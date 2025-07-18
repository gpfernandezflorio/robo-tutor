/* eslint-disable no-underscore-dangle */
/* A SourceReader represents the current position in a source file.
 * It keeps track of line and column numbers.
 * Methods are non-destructive. For example:
 *
 *     let r = new SourceReader('foo.gbs', 'if\n(True)');
 *
 *     r.peek();                       // ~~> 'i'
 *     r = r.consumeCharacter();       // Note: returns a new file reader.
 *
 *     r.peek();                       // ~~> 'f'
 *     r = r.consumeCharacter();
 *
 *     r.peek();                       // ~~> '\n'
 *     r = r.consumeCharacter('\n');
 *
 *     r.line();                       // ~~> 2
 */
class SourceReader {
    constructor(filename, string) {
        this._filename = filename; // Filename
        this._string = string; // Source of the current file
        this._index = 0; // Index in the current file
        this._line = 1; // Line in the current file
        this._column = 1; // Column in the current file
        this._regions = []; // Lexical (static) stack of regions
    }
    _clone() {
        const r = new SourceReader(this._filename, this._string);
        r._index = this._index;
        r._line = this._line;
        r._column = this._column;
        r._regions = this._regions;
        return r;
    }
    get filename() {
        return this._filename;
    }
    get line() {
        return this._line;
    }
    get column() {
        return this._column;
    }
    get region() {
        if (this._regions.length > 0) {
            return this._regions[0];
        }
        else {
            return '';
        }
    }
    /* Consume one character */
    consumeCharacter() {
        const r = this._clone();
        if (r.peek() === '\n') {
            r._line++;
            r._column = 1;
        }
        else {
            r._column++;
        }
        r._index++;
        return r;
    }
    /* Consume characters from the input, one per each character in the string
     * (the contents of the string are ignored). */
    consumeString(string) {
        let r = this._clone();
        // eslint-disable-next-line @typescript-eslint/no-unused-vars
        for (const _ of string) {
            r = r.consumeCharacter();
        }
        return r;
    }
    /* Returns the SourceReader after consuming an 'invisible' character.
     * Invisible characters affect the index but not the line or column.
     */
    consumeInvisibleCharacter() {
        const r = this._clone();
        r._index++;
        return r;
    }
    /* Consume 'invisible' characters from the input, one per each character
     * in the string */
    consumeInvisibleString(string) {
        // eslint-disable-next-line @typescript-eslint/no-this-alias
        let r = this;
        // eslint-disable-next-line @typescript-eslint/no-unused-vars
        for (const _ of string) {
            r = r.consumeInvisibleCharacter();
        }
        return r;
    }
    /* Return true if the substring occurs at the current point. */
    startsWith(sub) {
        const i = this._index;
        const j = this._index + sub.length;
        return j <= this._string.length && this._string.substring(i, j) === sub;
    }
    /* Return true if we have reached the end of the current file */
    eof() {
        return this._index >= this._string.length;
    }
    /* Return the current character, assuming we have not reached EOF */
    peek() {
        return this._string[this._index];
    }
    /* Push a region to the stack of regions (non-destructively) */
    beginRegion(region) {
        const r = this._clone();
        r._regions = [region].concat(r._regions);
        return r;
    }
    /* Pop a region from the stack of regions (non-destructively) */
    endRegion() {
        const r = this._clone();
        if (r._regions.length > 0) {
            r._regions = r._regions.slice(1);
        }
        return r;
    }
}
/* Return a source reader that represents an unknown position */
const UnknownPosition = new SourceReader('(?)', '');
/* An instance of MultifileReader represents a scanner for reading
 * source code from a list of files.
 */
class MultifileReader {
    /* The 'input' parameter should be either:
     * (1) a string. e.g.  'program {}', or
     * (2) a map from filenames to strings, e.g.
     *     {
     *       'foo.gbs': 'program { P() }',
     *       'bar.gbs': 'procedure P() {}',
     *     }
     */
    constructor(input) {
        if (typeof input === 'string') {
            input = { '(?)': input };
        }
        this._filenames = Object.keys(input);
        this._filenames.sort();
        this._input = input;
        this._index = 0;
    }
    /* Return true if there are more files */
    moreFiles() {
        return this._index + 1 < this._filenames.length;
    }
    /* Advance to the next file */
    nextFile() {
        this._index++;
    }
    /* Return a SourceReader for the current files */
    readCurrentFile() {
        if (this._index < this._filenames.length) {
            const filename = this._filenames[this._index];
            return new SourceReader(filename, this._input[filename]);
        }
        else {
            return new SourceReader('(?)', '');
        }
    }
}

/* Token tags are constant symbols */
const T_EOF = Symbol.for('T_EOF'); // End of file
const T_NUM = Symbol.for('T_NUM'); // Number
const T_STRING = Symbol.for('T_STRING'); // String constant
const T_UPPERID = Symbol.for('T_UPPERID'); // Uppercase identifier
const T_LOWERID = Symbol.for('T_LOWERID'); // Lowercase identifier
/* Keywords */
const T_PROGRAM = Symbol.for('T_PROGRAM');
const T_INTERACTIVE = Symbol.for('T_INTERACTIVE');
const T_PROCEDURE = Symbol.for('T_PROCEDURE');
const T_FUNCTION = Symbol.for('T_FUNCTION');
const T_RETURN = Symbol.for('T_RETURN');
const T_IF = Symbol.for('T_IF');
const T_THEN = Symbol.for('T_THEN');
const T_ELSEIF = Symbol.for('T_ELSEIF');
const T_ELSE = Symbol.for('T_ELSE');
const T_CHOOSE = Symbol.for('T_CHOOSE');
const T_WHEN = Symbol.for('T_WHEN');
const T_OTHERWISE = Symbol.for('T_OTHERWISE');
const T_MATCHING = Symbol.for('T_MATCHING');
const T_SELECT = Symbol.for('T_SELECT');
const T_ON = Symbol.for('T_ON');
const T_REPEAT = Symbol.for('T_REPEAT');
const T_FOREACH = Symbol.for('T_FOREACH');
const T_IN = Symbol.for('T_IN');
const T_WHILE = Symbol.for('T_WHILE');
const T_SWITCH = Symbol.for('T_SWITCH');
const T_TO = Symbol.for('T_TO');
const T_LET = Symbol.for('T_LET');
const T_NOT = Symbol.for('T_NOT');
const T_DIV = Symbol.for('T_DIV');
const T_MOD = Symbol.for('T_MOD');
const T_TYPE = Symbol.for('T_TYPE');
const T_IS = Symbol.for('T_IS');
const T_RECORD = Symbol.for('T_RECORD');
const T_VARIANT = Symbol.for('T_VARIANT');
const T_CASE = Symbol.for('T_CASE');
const T_FIELD = Symbol.for('T_FIELD');
const T_UNDERSCORE = Symbol.for('T_UNDERSCORE');
const T_TIMEOUT = Symbol.for('T_TIMEOUT');
/* Symbols */
const T_LPAREN = Symbol.for('T_LPAREN');
const T_RPAREN = Symbol.for('T_RPAREN');
const T_LBRACE = Symbol.for('T_LBRACE');
const T_RBRACE = Symbol.for('T_RBRACE');
const T_LBRACK = Symbol.for('T_LBRACK');
const T_RBRACK = Symbol.for('T_RBRACK');
const T_COMMA = Symbol.for('T_COMMA');
const T_SEMICOLON = Symbol.for('T_SEMICOLON');
const T_ELLIPSIS = Symbol.for('T_ELLIPSIS');
const T_RANGE = Symbol.for('T_RANGE');
const T_GETS = Symbol.for('T_GETS');
const T_PIPE = Symbol.for('T_PIPE');
const T_ARROW = Symbol.for('T_ARROW');
const T_ASSIGN = Symbol.for('T_ASSIGN');
const T_EQ = Symbol.for('T_EQ');
const T_NE = Symbol.for('T_NE');
const T_LE = Symbol.for('T_LE');
const T_GE = Symbol.for('T_GE');
const T_LT = Symbol.for('T_LT');
const T_GT = Symbol.for('T_GT');
const T_AND = Symbol.for('T_AND');
const T_OR = Symbol.for('T_OR');
const T_CONCAT = Symbol.for('T_CONCAT');
const T_PLUS = Symbol.for('T_PLUS');
const T_MINUS = Symbol.for('T_MINUS');
const T_TIMES = Symbol.for('T_TIMES');
const T_POW = Symbol.for('T_POW');
/* A token is given by:
 * - A token tag (e.g. T_LOWERID, T_NUM).
 * - Possibly, a value (e.g. 'nroBolitas', 8).
 *   When the value is irrelevant, we provide null by convention.
 * - Two positions, representing its location in the source. */
class Token {
    constructor(tag, value, startPos, endPos) {
        this._tag = tag;
        this._value = value;
        this._startPos = startPos;
        this._endPos = endPos;
    }
    toString() {
        const _tag = this._tag;
        const tag = typeof _tag === 'symbol' ? Symbol.keyFor(_tag).substring(2) : _tag;
        switch (tag) {
            case 'NUM':
            case 'STRING':
            case 'UPPERID':
            case 'LOWERID':
                return tag + '("' + this._value.toString() + '")';
            default:
                return tag;
        }
    }
    get tag() {
        return this._tag;
    }
    get value() {
        return this._value;
    }
    get startPos() {
        return this._startPos;
    }
    get endPos() {
        return this._endPos;
    }
}

/* eslint-disable camelcase */
const N_Main = Symbol.for('N_Main');
/* Definitions */
const N_DefProgram = Symbol.for('N_DefProgram');
const N_DefInteractiveProgram = Symbol.for('N_DefInteractiveProgram');
const N_DefProcedure = Symbol.for('N_DefProcedure');
const N_DefFunction = Symbol.for('N_DefFunction');
const N_DefType = Symbol.for('N_DefType');
/* Statements */
const N_StmtBlock = Symbol.for('N_StmtBlock');
const N_StmtReturn = Symbol.for('N_StmtReturn');
const N_StmtIf = Symbol.for('N_StmtIf');
const N_StmtRepeat = Symbol.for('N_StmtRepeat');
const N_StmtForeach = Symbol.for('N_StmtForeach');
const N_StmtWhile = Symbol.for('N_StmtWhile');
const N_StmtSwitch = Symbol.for('N_StmtSwitch');
const N_StmtAssignVariable = Symbol.for('N_StmtAssignVariable');
const N_StmtAssignTuple = Symbol.for('N_StmtAssignTuple');
const N_StmtProcedureCall = Symbol.for('N_StmtProcedureCall');
/* Patterns */
const N_PatternWildcard = Symbol.for('N_PatternWildcard');
const N_PatternVariable = Symbol.for('N_PatternVariable');
const N_PatternNumber = Symbol.for('N_PatternNumber');
const N_PatternStructure = Symbol.for('N_PatternStructure');
const N_PatternTuple = Symbol.for('N_PatternTuple');
const N_PatternTimeout = Symbol.for('N_PatternTimeout');
/* Expressions */
const N_ExprVariable = Symbol.for('N_ExprVariable');
const N_ExprConstantNumber = Symbol.for('N_ExprConstantNumber');
const N_ExprConstantString = Symbol.for('N_ExprConstantString');
const N_ExprChoose = Symbol.for('N_ExprChoose');
const N_ExprMatching = Symbol.for('N_ExprMatching');
const N_ExprList = Symbol.for('N_ExprList');
const N_ExprRange = Symbol.for('N_ExprRange');
const N_ExprTuple = Symbol.for('N_ExprTuple');
const N_ExprStructure = Symbol.for('N_ExprStructure');
const N_ExprStructureUpdate = Symbol.for('N_ExprStructureUpdate');
const N_ExprFunctionCall = Symbol.for('N_ExprFunctionCall');
/* SwitchBranch: pattern -> body */
const N_SwitchBranch = Symbol.for('N_SwitchBranch');
/* MatchingBranch: pattern -> body */
const N_MatchingBranch = Symbol.for('N_MatchingBranch');
/* FieldBinding: fieldName <- value */
const N_FieldBinding = Symbol.for('N_FieldBinding');
/* ConstructorDeclaration */
const N_ConstructorDeclaration = Symbol.for('N_ConstructorDeclaration');
/* Helper functions for the ASTNode toString method */
function indent(string) {
    const lines = [];
    for (const line of string.split('\n')) {
        lines.push('  ' + line);
    }
    return lines.join('\n');
}
function showAST(node) {
    if (node === undefined) {
        return 'null';
    }
    else if (node instanceof Array) {
        return '[\n' + showASTs(node).join(',\n') + '\n]';
    }
    else if (node instanceof Token) {
        return node.toString();
    }
    const tag = Symbol.keyFor(node.tag).substring(2);
    return tag + '(\n' + showASTs(node.children).join(',\n') + '\n)';
}
function showASTs(nodes) {
    const res = [];
    for (const node of nodes) {
        res.push(indent(showAST(node)));
    }
    return res;
}
/** An instance of ASTNode represents a node of the abstract syntax tree.
 * - tag should be a node tag symbol.
 * - children should be (recursively) a possibly empty array of ASTNode's.
 * - startPos and endPos represent the starting and ending
 *   position of the code fragment in the source code, to aid error
 *   reporting.
 **/
class ASTNode {
    constructor(tag, children) {
        this._tag = tag;
        this._children = children;
        this._startPos = UnknownPosition;
        this._endPos = UnknownPosition;
        this._attributes = {};
        /* Assert this invariant to protect against common mistakes. */
        if (!(children instanceof Array)) {
            throw Error('The children of an ASTNode should be an array.');
        }
    }
    toMulangLike() {
        return {
            tag: this._tag.toString().replace(/(^Symbol\(|\)$)/g, ''),
            contents: this._children.map((node) => {
                if (node === undefined) {
                    return 'null';
                }
                else if (node instanceof Array) {
                    return new ASTNode(Symbol('?'), node).toMulangLike().contents;
                }
                else if (node instanceof ASTNode) {
                    return node.toMulangLike();
                }
                else if (node instanceof Token) {
                    return node.toString();
                }
                else {
                    return '?';
                }
            })
        };
    }
    toString() {
        return showAST(this);
    }
    tagsToString() {
        this._tag = Symbol.keyFor(this._tag);
        for (let c of this._children) {
            if(c && ('tagsToString' in c)) {c.tagsToString();}
        }
    }
    get tag() {
        return this._tag;
    }
    get children() {
        return this._children;
    }
    set startPos(position) {
        this._startPos = position;
    }
    get startPos() {
        return this._startPos;
    }
    set endPos(position) {
        this._endPos = position;
    }
    get endPos() {
        return this._endPos;
    }
    get attributes() {
        return this._attributes;
    }
    set attributes(attributes) {
        this._attributes = attributes;
    }
}
/* Main */
class ASTMain extends ASTNode {
    constructor(definitions) {
        super(N_Main, definitions);
    }
    get definitions() {
        return this.children;
    }
}
/* Definitions */
class ASTDefProgram extends ASTNode {
    constructor(body) {
        super(N_DefProgram, [body]);
    }
    get body() {
        return this.children[0];
    }
}
class ASTNodeWithBranches extends ASTNode {
    get branches() {
        return this.children;
    }
}
class ASTDefInteractiveProgram extends ASTNodeWithBranches {
    constructor(branches) {
        super(N_DefInteractiveProgram, branches);
    }
    get branches() {
        return this.children;
    }
}
class ASTDefProcedure extends ASTNode {
    constructor(name, parameters, body) {
        super(N_DefProcedure, [name, parameters, body]);
    }
    get name() {
        return this.children[0];
    }
    get parameters() {
        return this.children[1];
    }
    get body() {
        return this.children[2];
    }
}
class ASTDefFunction extends ASTNode {
    constructor(name, parameters, body) {
        super(N_DefFunction, [name, parameters, body]);
    }
    get name() {
        return this.children[0];
    }
    get parameters() {
        return this.children[1];
    }
    get body() {
        return this.children[2];
    }
}
class ASTDefType extends ASTNode {
    constructor(typeName, constructorDeclarations) {
        super(N_DefType, [typeName, constructorDeclarations]);
    }
    get typeName() {
        return this.children[0];
    }
    get constructorDeclarations() {
        return this.children[1];
    }
}
/* Statements */
class ASTStmtBlock extends ASTNode {
    constructor(statements) {
        super(N_StmtBlock, statements);
    }
    get statements() {
        return this.children;
    }
}
class ASTStmtReturn extends ASTNode {
    constructor(result) {
        super(N_StmtReturn, [result]);
    }
    get result() {
        return this.children[0];
    }
}
class ASTStmtIf extends ASTNode {
    // Note: elseBlock may be null
    constructor(condition, thenBlock, elseBlock) {
        super(N_StmtIf, [condition, thenBlock, elseBlock]);
    }
    get condition() {
        return this.children[0];
    }
    get thenBlock() {
        return this.children[1];
    }
    get elseBlock() {
        return this.children[2];
    }
}
class ASTStmtRepeat extends ASTNode {
    constructor(times, body) {
        super(N_StmtRepeat, [times, body]);
    }
    get times() {
        return this.children[0];
    }
    get body() {
        return this.children[1];
    }
}
class ASTNodeWithPattern extends ASTNode {
    get pattern() {
        return this.children[0];
    }
}
class ASTStmtForeach extends ASTNodeWithPattern {
    constructor(pattern, range, body) {
        super(N_StmtForeach, [pattern, range, body]);
    }
    get pattern() {
        return this.children[0];
    }
    get range() {
        return this.children[1];
    }
    get body() {
        return this.children[2];
    }
}
class ASTStmtWhile extends ASTNode {
    constructor(condition, body) {
        super(N_StmtWhile, [condition, body]);
    }
    get condition() {
        return this.children[0];
    }
    get body() {
        return this.children[1];
    }
}
class ASTStmtSwitch extends ASTNodeWithBranches {
    constructor(subject, branches) {
        super(N_StmtSwitch, [subject, branches]);
    }
    get subject() {
        return this.children[0];
    }
    get branches() {
        return this.children[1];
    }
}
class ASTSwitchBranch extends ASTNodeWithPattern {
    constructor(pattern, body) {
        super(N_SwitchBranch, [pattern, body]);
    }
    get pattern() {
        return this.children[0];
    }
    get body() {
        return this.children[1];
    }
}
class ASTMatchingBranch extends ASTNodeWithPattern {
    constructor(pattern, body) {
        super(N_MatchingBranch, [pattern, body]);
    }
    get pattern() {
        return this.children[0];
    }
    get body() {
        return this.children[1];
    }
}
class ASTStmtAssignVariable extends ASTNode {
    constructor(variable, value) {
        super(N_StmtAssignVariable, [variable, value]);
    }
    get variable() {
        return this.children[0];
    }
    get value() {
        return this.children[1];
    }
}
class ASTStmtAssignTuple extends ASTNode {
    constructor(variables, value) {
        super(N_StmtAssignTuple, [variables, value]);
    }
    get variables() {
        return this.children[0];
    }
    get value() {
        return this.children[1];
    }
}
class ASTStmtProcedureCall extends ASTNode {
    constructor(procedureName, args) {
        super(N_StmtProcedureCall, [procedureName, args]);
    }
    get procedureName() {
        return this.children[0];
    }
    get args() {
        return this.children[1];
    }
}
class ASTPatternWildcard extends ASTNode {
    constructor(statement) {
        super(N_PatternWildcard, []);
    }
    get boundVariables() {
        return [];
    }
}
class ASTPatternVariable extends ASTNode {
    constructor(variableName) {
        super(N_PatternVariable, [variableName]);
    }
    get variableName() {
        return this.children[0];
    }
    get boundVariables() {
        return [this.children[0]];
    }
}
class ASTPatternNumber extends ASTNode {
    constructor(number) {
        super(N_PatternNumber, [number]);
    }
    get number() {
        return this.children[0];
    }
    get boundVariables() {
        return [];
    }
}
class ASTPatternStructure extends ASTNode {
    constructor(constructorName, parameters) {
        super(N_PatternStructure, [constructorName, parameters]);
    }
    get constructorName() {
        return this.children[0];
    }
    get boundVariables() {
        return this.children[1];
    }
}
class ASTPatternTuple extends ASTNode {
    constructor(parameters) {
        super(N_PatternTuple, parameters);
    }
    get boundVariables() {
        return this.children;
    }
}
class ASTPatternTimeout extends ASTNode {
    constructor(timeout) {
        super(N_PatternTimeout, [timeout]);
    }
    get boundVariables() {
        return [];
    }
    get timeout() {
        return parseInt(this.children[0].value, 10);
    }
}
class ASTExprVariable extends ASTNode {
    constructor(variableName) {
        super(N_ExprVariable, [variableName]);
    }
    get variableName() {
        return this.children[0];
    }
}
class ASTExprConstantNumber extends ASTNode {
    constructor(number) {
        super(N_ExprConstantNumber, [number]);
    }
    get number() {
        return this.children[0];
    }
}
class ASTExprConstantString extends ASTNode {
    constructor(string) {
        super(N_ExprConstantString, [string]);
    }
    get string() {
        return this.children[0];
    }
}
class ASTExprChoose extends ASTNode {
    constructor(condition, trueExpr, falseExpr) {
        super(N_ExprChoose, [condition, trueExpr, falseExpr]);
    }
    get condition() {
        return this.children[0];
    }
    get trueExpr() {
        return this.children[1];
    }
    get falseExpr() {
        return this.children[2];
    }
}
class ASTExprMatching extends ASTNodeWithBranches {
    constructor(subject, branches) {
        super(N_ExprMatching, [subject, branches]);
    }
    get subject() {
        return this.children[0];
    }
    get branches() {
        return this.children[1];
    }
}
class ASTExprList extends ASTNode {
    constructor(elements) {
        super(N_ExprList, elements);
    }
    get elements() {
        return this.children;
    }
}
class ASTExprRange extends ASTNode {
    // Note: second may be null
    constructor(first, second, last) {
        super(N_ExprRange, [first, second, last]);
    }
    get first() {
        return this.children[0];
    }
    get second() {
        return this.children[1];
    }
    get last() {
        return this.children[2];
    }
}
class ASTExprTuple extends ASTNode {
    constructor(elements) {
        super(N_ExprTuple, elements);
    }
    get elements() {
        return this.children;
    }
}
class ASTExprStructure extends ASTNode {
    constructor(constructorName, fieldBindings) {
        super(N_ExprStructure, [constructorName, fieldBindings]);
    }
    get constructorName() {
        return this.children[0];
    }
    get fieldBindings() {
        return this.children[1];
    }
    fieldNames() {
        const names = [];
        for (const fieldBinding of this.fieldBindings) {
            names.push(fieldBinding.fieldName.value);
        }
        return names;
    }
}
class ASTExprStructureUpdate extends ASTNode {
    constructor(constructorName, original, fieldBindings) {
        super(N_ExprStructureUpdate, [constructorName, original, fieldBindings]);
    }
    get constructorName() {
        return this.children[0];
    }
    get original() {
        return this.children[1];
    }
    get fieldBindings() {
        return this.children[2];
    }
    fieldNames() {
        const names = [];
        for (const fieldBinding of this.fieldBindings) {
            names.push(fieldBinding.fieldName.value);
        }
        return names;
    }
}
class ASTExprFunctionCall extends ASTNode {
    constructor(functionName, args) {
        super(N_ExprFunctionCall, [functionName, args]);
    }
    get functionName() {
        return this.children[0];
    }
    get args() {
        return this.children[1];
    }
}
class ASTFieldBinding extends ASTNode {
    constructor(fieldName, value) {
        super(N_FieldBinding, [fieldName, value]);
    }
    get fieldName() {
        return this.children[0];
    }
    get value() {
        return this.children[1];
    }
}
class ASTConstructorDeclaration extends ASTNode {
    constructor(constructorName, fieldNames) {
        super(N_ConstructorDeclaration, [constructorName, fieldNames]);
    }
    get constructorName() {
        return this.children[0];
    }
    get fieldNames() {
        return this.children[1];
    }
}

/* eslint-disable camelcase */
/* eslint-disable @typescript-eslint/explicit-function-return-type */
/* eslint-disable quote-props */
/* istanbul ignore file */
const keyword$1$1 = (palabra) => 'la palabra clave "' + palabra + '"';
function pluralize$1$1(n, singular, plural) {
    if (n === 0) {
        return 'ningún ' + singular;
    }
    else if (n === 1) {
        return 'un ' + singular;
    }
    else {
        return n.toString() + ' ' + plural;
    }
}
// Only for typing purposes
// eslint-disable-next-line @typescript-eslint/ban-types
const toFunc$2 = (x) => x;
function ordinalNumber$1(n) {
    const units = [
        '',
        'primer',
        'segundo',
        'tercer',
        'cuarto',
        'quinto',
        'sexto',
        'séptimo',
        'octavo',
        'noveno'
    ];
    if (n >= 1 && n <= 9) {
        return units[n];
    }
    else {
        return '#' + n.toString();
    }
}
function describeType$1(type) {
    if (type.isInteger()) {
        return ['m', 'número', 'números'];
    }
    else if (type.isBoolean()) {
        return ['m', 'booleano', 'booleanos'];
    }
    else if (type.isColor()) {
        return ['m', 'color', 'colores'];
    }
    else if (type.isDirection()) {
        return ['f', 'dirección', 'direcciones'];
    }
    else if (type.isList() && type.contentType.isAny()) {
        return ['f', 'lista', 'listas'];
    }
    else if (type.isList()) {
        const description = describeType$1(type.contentType);
        if (description === undefined) {
            return undefined;
        }
        else {
            const plural = description[2];
            return ['f', 'lista de ' + plural, 'listas de ' + plural];
        }
    }
    else {
        return undefined;
    }
}
function describeTypeSingular$1(type) {
    const description = describeType$1(type);
    if (description === undefined) {
        return type.toString();
    }
    else {
        const singular = description[1];
        return singular;
    }
}
function typeAsNoun$1(type) {
    const description = describeType$1(type);
    if (description === undefined) {
        return 'un valor de tipo ' + type.toString();
    }
    else {
        const gender = description[0];
        const singular = description[1];
        if (gender === 'm') {
            return 'un ' + singular;
        }
        else {
            return 'una ' + singular;
        }
    }
}
function typeAsQualifierSingular$1(type) {
    const description = describeType$1(type);
    if (description === undefined) {
        return 'de tipo ' + type.toString();
    }
    else {
        const gender = description[0];
        const singular = description[1];
        if (gender === 'm') {
            return 'un ' + singular;
        }
        else {
            return 'una ' + singular;
        }
    }
}
function typeAsQualifierPlural$1(type) {
    const description = describeType$1(type);
    if (description === undefined) {
        return 'de tipo ' + type.toString();
    }
    else {
        const gender = description[0];
        const plural = description[2];
        if (gender === 'm') {
            return plural;
        }
        else {
            return plural;
        }
    }
}
function listOfTypes$1(types) {
    const typeStrings = [];
    for (const type of types) {
        typeStrings.push(describeTypeSingular$1(type));
    }
    return typeStrings.join(', ');
}
function openingDelimiterName$1(delimiter) {
    if (delimiter === '(' || delimiter === ')') {
        return 'un paréntesis abierto "("';
    }
    else if (delimiter === '[' || delimiter === ']') {
        return 'un corchete abierto "["';
    }
    else if (delimiter === '{' || delimiter === '}') {
        return 'una llave abierta "{"';
    }
    else {
        return delimiter;
    }
}
function formatTypes$1(string, type1, type2) {
    let result = '';
    for (let i = 0; i < string.length; i++) {
        if (string[i] === '%' && i + 1 < string.length) {
            if (string[i + 1] === '%') {
                result += '%';
                i++;
            }
            else if (string[i + 1] === '1') {
                result += typeAsNoun$1(type1);
                i++;
            }
            else if (string[i + 1] === '2') {
                result += typeAsNoun$1(type2);
                i++;
            }
            else {
                result += '%';
            }
        }
        else {
            result += string[i];
        }
    }
    return result;
}
// eslint-disable-next-line @typescript-eslint/ban-types
const LOCALE_ES$1 = {
    /* Descriptions of syntactic constructions and tokens */
    definition: 'una definición (de programa, función, procedimiento, o tipo)',
    pattern: 'un patrón (comodín "_", constructor aplicado a variables, o tupla)',
    statement: 'un comando',
    expression: 'una expresión',
    'procedure call': 'una invocación a un procedimiento',
    'field name': 'el nombre de un campo',
    T_EOF: 'el final del archivo',
    T_NUM: 'un número',
    T_STRING: 'una cadena (string)',
    T_UPPERID: 'un identificador con mayúsculas',
    T_LOWERID: 'un identificador con minúsculas',
    T_PROGRAM: keyword$1$1('program'),
    T_INTERACTIVE: keyword$1$1('interactive'),
    T_PROCEDURE: keyword$1$1('procedure'),
    T_FUNCTION: keyword$1$1('function'),
    T_RETURN: keyword$1$1('return'),
    T_IF: keyword$1$1('if'),
    T_THEN: keyword$1$1('then'),
    T_ELSE: keyword$1$1('else'),
    T_REPEAT: keyword$1$1('repeat'),
    T_FOREACH: keyword$1$1('foreach'),
    T_IN: keyword$1$1('in'),
    T_WHILE: keyword$1$1('while'),
    T_SWITCH: keyword$1$1('switch'),
    T_TO: keyword$1$1('to'),
    T_LET: keyword$1$1('let'),
    T_NOT: keyword$1$1('not'),
    T_DIV: keyword$1$1('div'),
    T_MOD: keyword$1$1('mod'),
    T_TYPE: keyword$1$1('type'),
    T_IS: keyword$1$1('is'),
    T_CHOOSE: keyword$1$1('choose'),
    T_WHEN: keyword$1$1('when'),
    T_OTHERWISE: keyword$1$1('otherwise'),
    T_MATCHING: keyword$1$1('matching'),
    T_SELECT: keyword$1$1('select'),
    T_ON: keyword$1$1('on'),
    T_RECORD: keyword$1$1('record'),
    T_VARIANT: keyword$1$1('variant'),
    T_CASE: keyword$1$1('case'),
    T_FIELD: keyword$1$1('field'),
    T_UNDERSCORE: 'un guión bajo ("_")',
    T_LPAREN: 'un paréntesis izquierdo ("(")',
    T_RPAREN: 'un paréntesis derecho (")")',
    T_LBRACE: 'una llave izquierda ("{")',
    T_RBRACE: 'una llave derecha ("}")',
    T_LBRACK: 'un corchete izquierdo ("[")',
    T_RBRACK: 'un corchete derecho ("]")',
    T_COMMA: 'una coma (",")',
    T_SEMICOLON: 'un punto y coma (";")',
    T_RANGE: 'un separador de rango ("..")',
    T_GETS: 'una flecha hacia la izquierda ("<-")',
    T_PIPE: 'una barra vertical ("|")',
    T_ARROW: 'una flecha ("->")',
    T_ASSIGN: 'un operador de asignación (":=")',
    T_EQ: 'una comparación por igualdad ("==")',
    T_NE: 'una comparación por desigualdad ("/=")',
    T_LE: 'un menor o igual ("<=")',
    T_GE: 'un mayor o igual (">=")',
    T_LT: 'un menor estricto ("<")',
    T_GT: 'un mayor estricto (">")',
    T_AND: 'el "y" lógico ("&&")',
    T_OR: 'el "o" lógico ("||")',
    T_CONCAT: 'el operador de concatenación de listas ("++")',
    T_PLUS: 'el operador de suma ("+")',
    T_MINUS: 'el operador de resta ("-")',
    T_TIMES: 'el operador de producto ("*")',
    T_POW: 'el operador de potencia ("^")',
    /* Local name categories */
    LocalVariable: 'variable',
    LocalIndex: 'índice',
    LocalParameter: 'parámetro',
    /* Descriptions of value types */
    V_Integer: 'un número',
    V_String: 'una cadena',
    V_Tuple: 'una tupla',
    V_List: 'una lista',
    V_Structure: 'una estructura',
    /* Lexer */
    'errmsg:unclosed-multiline-comment': 'El comentario se abre pero nunca se cierra.',
    'errmsg:unclosed-string-constant': 'La comilla que abre no tiene una comilla que cierra correspondiente.',
    // eslint-disable-next-line max-len
    'errmsg:numeric-constant-should-not-have-leading-zeroes': `Las constantes numéricas no se pueden escribir con ceros a la izquierda.`,
    // eslint-disable-next-line max-len
    'errmsg:identifier-must-start-with-alphabetic-character': `Los identificadores deben empezar con un caracter alfabético (a...z,A...Z).`,
    'errmsg:unknown-token': (symbol) => 'Símbolo desconocido en la entrada: "' + symbol + '".',
    'warning:empty-pragma': 'Directiva pragma vacía.',
    'warning:unknown-pragma': (pragmaName) => 'Directiva pragma desconocida: "' + pragmaName + '".',
    'errmsg:unmatched-opening-delimiter': (delimiter) => 'Se encontró ' + openingDelimiterName$1(delimiter) + ' pero nunca se cierra.',
    'errmsg:unmatched-closing-delimiter': (delimiter) => 'Se encontró un "' +
        delimiter +
        '" ' +
        'pero no había ' +
        openingDelimiterName$1(delimiter) +
        '.',
    'errmsg:unknown-language-option': (option) => 'Opción desconocida. "' + option + '".',
    /* Parser */
    'errmsg:empty-source': 'El programa está vacío.',
    'errmsg:expected-but-found': (expected, found) => `Se esperaba ${expected}. Se encontró: ${found}.`,
    'errmsg:pattern-number-cannot-be-negative-zero': 'El patrón numérico no puede ser "-0".',
    'errmsg:return-tuple-cannot-be-empty': 'El return tiene que devolver algo.',
    'errmsg:pattern-tuple-cannot-be-singleton': 'El patrón para una tupla no puede tener una sola componente. ' +
        'Las tuplas tienen 0, 2, 3, o más componentes, pero no 1.',
    'errmsg:assignment-tuple-cannot-be-singleton': 'La asignación a una tupla no puede constar de una sola componente. ' +
        'Las tuplas tienen 0, 2, 3, o más componentes, pero no 1.',
    'errmsg:operators-are-not-associative': (op1, op2) => 'La expresión usa ' +
        op1 +
        ' y ' +
        op2 +
        ', pero estos operadores no se pueden asociar. ' +
        'Quizás faltan paréntesis.',
    'errmsg:obsolete-tuple-assignment': 'Se esperaba un comando pero se encontró un paréntesis izquierdo. ' +
        'Nota: la sintaxis de asignación de tuplas "(x1, ..., xN) := y" ' +
        'está obsoleta. Usar "let (x1, ..., xN) := y".',
    /* Linter */
    'errmsg:program-already-defined': (pos1, pos2) => 'Ya había un programa definido en ' +
        pos1 +
        '.\n' +
        'No se puede definir un programa en ' +
        pos2 +
        '.',
    'errmsg:procedure-already-defined': (name, pos1, pos2) => 'El procedimiento "' +
        name +
        '" está definido dos veces: ' +
        'en ' +
        pos1 +
        ' y en ' +
        pos2 +
        '.',
    'errmsg:function-already-defined': (name, pos1, pos2) => 'La función "' +
        name +
        '" está definida dos veces: ' +
        'en ' +
        pos1 +
        ' y en ' +
        pos2 +
        '.',
    'errmsg:type-already-defined': (name, pos1, pos2) => `El tipo "${name}" está definido dos veces: en ${pos1} y en ${pos2}.`,
    'errmsg:constructor-already-defined': (name, pos1, pos2) => 'El constructor "' +
        name +
        '" está definido dos veces: ' +
        'en ' +
        pos1 +
        ' y en ' +
        pos2 +
        '.',
    'errmsg:repeated-field-name': (constructorName, fieldName) => 'El campo "' +
        fieldName +
        '" no puede estar repetido ' +
        'para el constructor "' +
        constructorName +
        '".',
    'errmsg:function-and-field-cannot-have-the-same-name': (name, posFunction, posField) => 'El nombre "' +
        name +
        '" se usa ' +
        'para una función en ' +
        posFunction +
        ' y ' +
        'para un campo en ' +
        posField +
        '.',
    'errmsg:source-should-have-a-program-definition': 
    /* Note: the code may actually be completely empty, but
     * we avoid this technicality since the message could be
     * confusing. */
    'El código debe tener una definición de "program { ... }".',
    'errmsg:procedure-should-not-have-return': (name) => `El procedimiento "${name}" no debería tener un comando "return".`,
    'errmsg:function-should-have-return': (name) => 'La función "' + name + '" debería tener un comando "return".',
    'errmsg:return-statement-not-allowed-here': 'El comando "return" solo puede aparecer como el último comando ' +
        'de una función o como el último comando del programa.',
    'errmsg:local-name-conflict': (name, oldCat, oldPos, newCat, newPos) => 'Conflicto de nombres: "' +
        name +
        '" se usa dos veces: ' +
        'como ' +
        oldCat +
        ' en ' +
        oldPos +
        ', y ' +
        'como ' +
        newCat +
        ' en ' +
        newPos +
        '.',
    'errmsg:repeated-variable-in-tuple-assignment': (name) => `La variable "${name}" está repetida en la asignación de tuplas.`,
    'errmsg:constructor-used-as-procedure': (name, type) => 'El procedimiento "' +
        name +
        '" no está definido. ' +
        'El nombre "' +
        name +
        '" es el nombre de un constructor ' +
        'del tipo "' +
        type +
        '".',
    'errmsg:undefined-procedure': (name) => 'El procedimiento "' + name + '" no está definido.',
    'errmsg:undefined-function': (name) => 'La función "' + name + '" no está definida.',
    'errmsg:procedure-arity-mismatch': (name, expected, received) => '"El procedimiento "' +
        name +
        '" espera recibir ' +
        toFunc$2(LOCALE_ES$1['<n>-parameters'])(expected) +
        ' pero se lo invoca con ' +
        toFunc$2(LOCALE_ES$1['<n>-arguments'])(received) +
        '.',
    'errmsg:function-arity-mismatch': (name, expected, received) => 'La función "' +
        name +
        '" espera recibir ' +
        toFunc$2(LOCALE_ES$1['<n>-parameters'])(expected) +
        ' pero se la invoca con ' +
        toFunc$2(LOCALE_ES$1['<n>-arguments'])(received) +
        '.',
    'errmsg:structure-pattern-arity-mismatch': (name, expected, received) => 'El constructor "' +
        name +
        '" tiene ' +
        toFunc$2(LOCALE_ES$1['<n>-fields'])(expected) +
        ' pero el patrón tiene ' +
        toFunc$2(LOCALE_ES$1['<n>-parameters'])(received) +
        '.',
    'errmsg:type-used-as-constructor'(name, constructorNames) {
        let msg;
        if (constructorNames.length === 0) {
            msg = '(no tiene constructores).';
        }
        else if (constructorNames.length === 1) {
            msg = '(tiene un constructor: ' + constructorNames[0] + ').';
        }
        else {
            msg = '(sus constructores son: ' + constructorNames.join(', ') + ').';
        }
        return ('El constructor "' +
            name +
            '" no está definido. ' +
            'El nombre "' +
            name +
            '" es el nombre de un tipo ' +
            msg);
    },
    'errmsg:procedure-used-as-constructor': (name) => 'El constructor "' +
        name +
        '" no está definido. ' +
        'El nombre "' +
        name +
        '" es el nombre de un procedimiento.',
    'errmsg:undeclared-constructor': (name) => 'El constructor "' + name + '" no está definido.',
    'errmsg:wildcard-pattern-should-be-last': 'El comodín "_" debe estar en la última rama.',
    'errmsg:variable-pattern-should-be-last': (name) => 'El patrón variable "' + name + '" tiene debe estar en la última rama.',
    'errmsg:numeric-pattern-repeats-number': (number) => 'Hay dos ramas distintas para el número "' + number + '".',
    'errmsg:structure-pattern-repeats-constructor': (name) => 'Hay dos ramas distintas para el constructor "' + name + '".',
    'errmsg:structure-pattern-repeats-tuple-arity': (arity) => 'Hay dos ramas distintas para las tuplas de ' + arity.toString() + ' componentes.',
    'errmsg:structure-pattern-repeats-timeout': 'Hay dos ramas distintas para el TIMEOUT.',
    'errmsg:pattern-does-not-match-type': (expectedType, patternType) => 'Los patrones tienen que ser todos del mismo tipo. ' +
        'El patrón debería ser de tipo ' +
        expectedType +
        'pero es de tipo ' +
        patternType +
        '.',
    'errmsg:patterns-in-interactive-program-must-be-events': 'Los patrones de un "interactive program" deben ser eventos.',
    'errmsg:patterns-in-interactive-program-cannot-be-variables': 'El patrón no puede ser una variable.',
    'errmsg:patterns-in-switch-must-not-be-events': 'El patrón no puede ser un evento.',
    'errmsg:structure-construction-repeated-field': (constructorName, fieldName) => 'El campo "' +
        fieldName +
        '" está repetido en ' +
        'la instanciación del constructor "' +
        constructorName +
        '".',
    'errmsg:structure-construction-invalid-field': (constructorName, fieldName) => 'El campo "' +
        fieldName +
        '" no es un campo válido ' +
        'para el constructor "' +
        constructorName +
        '".',
    'errmsg:structure-construction-missing-field': (constructorName, fieldName) => 'Falta darle valor al campo "' +
        fieldName +
        '" ' +
        'del constructor "' +
        constructorName +
        '".',
    'errmsg:structure-construction-cannot-be-an-event': (constructorName) => 'El constructor "' +
        constructorName +
        '" corresponde a un ' +
        'evento, y solamente se puede manejar implícitamente ' +
        'en un programa interactivo (el usuario no puede construir ' +
        'instancias).',
    'errmsg:forbidden-extension-destructuring-foreach': 'El índice de la repetición indexada debe ser un identificador.',
    ['errmsg:forbidden-extension-allow-recursion']: (cycle) => {
        const msg = [];
        for (const call of cycle) {
            msg.push('  ' +
                call.caller +
                ' llama a ' +
                call.callee +
                ' (' +
                call.location.startPos.filename.toString() +
                ':' +
                call.location.startPos.line.toString() +
                ':' +
                call.location.startPos.column.toString() +
                ')');
        }
        return ('La recursión está deshabilitada. ' +
            'Hay un ciclo en las invocaciones:\n' +
            msg.join('\n'));
    },
    'errmsg:patterns-in-foreach-must-not-be-events': 'El patrón de un foreach no puede ser un evento.',
    /* Runtime errors (virtual machine) */
    'errmsg:ellipsis': 'El programa todavía no está completo.',
    'errmsg:undefined-variable': (variableName) => 'La variable "' + variableName + '" no está definida.',
    'errmsg:too-few-arguments': (routineName) => 'Faltan argumentos para "' + routineName + '".',
    'errmsg:expected-structure-but-got': (constructorName, valueTag) => 'Se esperaba una estructura construida ' +
        'con el constructor "' +
        constructorName +
        '", ' +
        'pero se recibió ' +
        valueTag +
        '.',
    'errmsg:expected-constructor-but-got': (constructorNameExpected, constructorNameReceived) => 'Se esperaba una estructura construida ' +
        'con el constructor "' +
        constructorNameExpected +
        '", ' +
        'pero el constructor recibido es ' +
        constructorNameReceived +
        '".',
    'errmsg:incompatible-types-on-assignment': (variableName, oldType, newType) => 'La variable "' +
        variableName +
        '" ' +
        'contenía ' +
        typeAsNoun$1(oldType) +
        ', ' +
        'no se le puede asignar ' +
        typeAsNoun$1(newType) +
        '".',
    'errmsg:incompatible-types-on-list-creation': (index, oldType, newType) => 'Todos los elementos de una lista deben ser del mismo tipo. ' +
        'Los elementos son ' +
        typeAsQualifierPlural$1(oldType) +
        ', ' +
        'pero el elemento en la posición ' +
        index.toString() +
        ' ' +
        'es ' +
        typeAsQualifierSingular$1(newType) +
        '.',
    'errmsg:incompatible-types-on-structure-update': (fieldName, oldType, newType) => 'El campo "' +
        fieldName +
        '" es ' +
        typeAsQualifierSingular$1(oldType) +
        '. ' +
        'No se lo puede actualizar con ' +
        typeAsNoun$1(newType) +
        '.',
    'errmsg:expected-tuple-value-but-got': (receivedType) => 'Se esperaba una tupla pero se recibió ' + typeAsNoun$1(receivedType) + '.',
    'errmsg:tuple-component-out-of-bounds': (size, index) => 'Índice fuera de rango. ' +
        'La tupla es de tamaño ' +
        size.toString() +
        ' y ' +
        'el índice es ' +
        index.toString() +
        '.',
    'errmsg:expected-structure-value-but-got': (receivedType) => 'Se esperaba una estructura pero se recibió ' + typeAsNoun$1(receivedType) + '.',
    'errmsg:structure-field-not-present': (fieldNames, missingFieldName) => 'La estructura no tiene un campo "' +
        missingFieldName +
        '". ' +
        'Los campos son: [' +
        fieldNames.join(', ') +
        '].',
    'errmsg:primitive-does-not-exist': (primitiveName) => `La operación primitiva "${primitiveName}" no existe o no está disponible.`,
    'errmsg:primitive-arity-mismatch': (name, expected, received) => 'La operación "' +
        name +
        '" espera recibir ' +
        toFunc$2(LOCALE_ES$1['<n>-parameters'])(expected) +
        ' pero se la invoca con ' +
        toFunc$2(LOCALE_ES$1['<n>-arguments'])(received) +
        '.',
    'errmsg:primitive-argument-type-mismatch'(name, parameterIndex, numArgs, expectedType, receivedType) {
        let msg = 'El ';
        if (numArgs > 1) {
            msg += ordinalNumber$1(parameterIndex) + ' ';
        }
        msg += 'parámetro ';
        msg += 'de "' + name + '" ';
        msg += 'debería ser ' + typeAsQualifierSingular$1(expectedType) + ' ';
        msg += 'pero es ' + typeAsQualifierSingular$1(receivedType) + '.';
        return msg;
    },
    'errmsg:expected-value-of-type-but-got': (expectedType, receivedType) => 'Se esperaba ' +
        typeAsNoun$1(expectedType) +
        ' ' +
        'pero se recibió ' +
        typeAsNoun$1(receivedType) +
        '.',
    'errmsg:expected-value-of-some-type-but-got': (expectedTypes, receivedType) => 'Se esperaba un valor de alguno de los siguientes tipos: ' +
        listOfTypes$1(expectedTypes) +
        '. ' +
        'Pero se recibió ' +
        typeAsNoun$1(receivedType) +
        '.',
    'errmsg:expected-values-to-have-compatible-types': (type1, type2) => 'Los tipos de las expresiones no coinciden: ' +
        'la primera es ' +
        typeAsQualifierSingular$1(type1) +
        ' ' +
        'y la segunda es ' +
        typeAsQualifierSingular$1(type2) +
        '.',
    'errmsg:switch-does-not-match': 'El valor analizado no coincide con ninguna de las ramas del switch.',
    'errmsg:foreach-pattern-does-not-match': 'El elemento no coincide con el patrón esperado por el foreach.',
    'errmsg:cannot-divide-by-zero': 'No se puede dividir por cero.',
    'errmsg:negative-exponent': 'El exponente de la potencia no puede ser negativo.',
    'errmsg:list-cannot-be-empty': 'La lista no puede ser vacía.',
    'errmsg:timeout': (millisecs) => 'La ejecución del programa demoró más de ' + millisecs.toString() + 'ms.',
    /* Typecheck */
    'errmsg:typecheck-failed': (errorMessage, type1, type2) => formatTypes$1(errorMessage, type1, type2),
    /* Board operations */
    'errmsg:cannot-move-to': (dirName) => 'No se puede mover hacia la dirección ' + dirName + ': cae afuera del tablero.',
    'errmsg:cannot-remove-stone': (dirName) => 'No se puede sacar una bolita de color ' + dirName + ': no hay bolitas de ese color.',
    /* Runtime */
    'TYPE:Integer': 'Number',
    'TYPE:String': 'String',
    'TYPE:Tuple': '',
    'TYPE:List': 'List',
    'TYPE:Event': 'Event',
    'CONS:INIT': 'INIT',
    'CONS:TIMEOUT': 'TIMEOUT',
    'TYPE:Bool': 'Bool',
    'CONS:False': 'False',
    'CONS:True': 'True',
    'TYPE:Color': 'Color',
    'CONS:Color0': 'Azul',
    'CONS:Color1': 'Negro',
    'CONS:Color2': 'Rojo',
    'CONS:Color3': 'Verde',
    'TYPE:Dir': 'Dir',
    'CONS:Dir0': 'Norte',
    'CONS:Dir1': 'Este',
    'CONS:Dir2': 'Sur',
    'CONS:Dir3': 'Oeste',
    'PRIM:TypeCheck': 'TypeCheck',
    'PRIM:BOOM': 'BOOM',
    'PRIM:boom': 'boom',
    'PRIM:PutStone': 'Poner',
    'PRIM:RemoveStone': 'Sacar',
    'PRIM:Move': 'Mover',
    'PRIM:GoToEdge': 'IrAlBorde',
    'PRIM:EmptyBoardContents': 'VaciarTablero',
    'PRIM:numStones': 'nroBolitas',
    'PRIM:anyStones': 'hayBolitas',
    'PRIM:canMove': 'puedeMover',
    'PRIM:next': 'siguiente',
    'PRIM:prev': 'previo',
    'PRIM:opposite': 'opuesto',
    'PRIM:minBool': 'minBool',
    'PRIM:maxBool': 'maxBool',
    'PRIM:minColor': 'minColor',
    'PRIM:maxColor': 'maxColor',
    'PRIM:minDir': 'minDir',
    'PRIM:maxDir': 'maxDir',
    'PRIM:isEmpty': 'esVacía',
    'PRIM:head': 'primero',
    'PRIM:tail': 'sinElPrimero',
    'PRIM:oldTail': 'resto',
    'PRIM:init': 'comienzo',
    'PRIM:last': 'último',
    /* Helpers */
    '<alternative>': (strings) => 'alguna de las siguientes alternativas:\n' +
        strings.map((s) => '  ' + s).join('\n'),
    '<position>': (filename, line, column) => filename + ':' + line.toString() + ':' + column.toString(),
    '<n>-parameters': (n) => pluralize$1$1(n, 'parámetro', 'parámetros'),
    '<n>-arguments': (n) => pluralize$1$1(n, 'argumento', 'argumentos'),
    '<n>-fields': (n) => pluralize$1$1(n, 'campo', 'campos'),
    '<pattern-type>'(patternType) {
        if (patternType === 'Event') {
            return 'evento del programa interactivo';
        }
        else if (patternType.substring(0, 7) === '_TUPLE_') {
            return 'tupla de ' + patternType.substring(7) + ' componentes';
        }
        else {
            return patternType;
        }
    }
};

const LOCALE_EN$1 = {};
for (const key in LOCALE_ES$1) {
    LOCALE_EN$1[key] = LOCALE_ES$1[key];
}
LOCALE_EN$1['TYPE:Color'] = 'Color';
LOCALE_EN$1['CONS:Color0'] = 'Blue';
LOCALE_EN$1['CONS:Color1'] = 'Black';
LOCALE_EN$1['CONS:Color2'] = 'Red';
LOCALE_EN$1['CONS:Color3'] = 'Green';
LOCALE_EN$1['TYPE:Dir'] = 'Dir';
LOCALE_EN$1['CONS:Dir0'] = 'North';
LOCALE_EN$1['CONS:Dir1'] = 'East';
LOCALE_EN$1['CONS:Dir2'] = 'South';
LOCALE_EN$1['CONS:Dir3'] = 'West';
LOCALE_EN$1['PRIM:PutStone'] = 'Drop';
LOCALE_EN$1['PRIM:RemoveStone'] = 'Grab';
LOCALE_EN$1['PRIM:Move'] = 'Move';
LOCALE_EN$1['PRIM:GoToEdge'] = 'GoToEdge';
LOCALE_EN$1['PRIM:EmptyBoardContents'] = 'EmptyBoardContents';
LOCALE_EN$1['PRIM:numStones'] = 'numStones';
LOCALE_EN$1['PRIM:anyStones'] = 'anyStones';
LOCALE_EN$1['PRIM:canMove'] = 'canMove';
LOCALE_EN$1['PRIM:next'] = 'next';
LOCALE_EN$1['PRIM:prev'] = 'prev';
LOCALE_EN$1['PRIM:opposite'] = 'opposite';
LOCALE_EN$1['PRIM:minBool'] = 'minBool';
LOCALE_EN$1['PRIM:maxBool'] = 'maxBool';
LOCALE_EN$1['PRIM:minColor'] = 'minColor';
LOCALE_EN$1['PRIM:maxColor'] = 'maxColor';
LOCALE_EN$1['PRIM:minDir'] = 'minDir';
LOCALE_EN$1['PRIM:maxDir'] = 'maxDir';
LOCALE_EN$1['PRIM:head'] = 'head';
LOCALE_EN$1['PRIM:tail'] = 'tail';
LOCALE_EN$1['PRIM:oldTail'] = 'tail';
LOCALE_EN$1['PRIM:init'] = 'init';
LOCALE_EN$1['PRIM:last'] = 'last';

const keyword$2 = (palabra) => `‘a palavra chave "${palabra}"`;
// Only for typing purposes
// eslint-disable-next-line @typescript-eslint/ban-types
const toFunc$1$1 = (x) => x;
function pluralize$2(n, singular, plural) {
    if (n === 0) {
        return 'nenhum ' + singular;
    }
    else if (n === 1) {
        return 'um ' + singular;
    }
    else {
        return n.toString() + ' ' + plural;
    }
}
const LOCALE_PT$1 = {};
for (const key in LOCALE_ES$1) {
    LOCALE_PT$1[key] = LOCALE_ES$1[key];
}
/* Descriptions of syntactic constructions and tokens */
LOCALE_PT$1['definition'] = 'uma definição (de programa, função, procedimento, ou tipo)';
LOCALE_PT$1['pattern'] = 'um padrão (comodín "_", construtor aplicado a variáveis, ou tupla)';
LOCALE_PT$1['statement'] = 'um comando';
LOCALE_PT$1['expression'] = 'uma expressão';
LOCALE_PT$1['procedure call'] = 'uma invocação a um procedimento';
LOCALE_PT$1['field name'] = 'o nome de um campo';
LOCALE_PT$1['T_EOF'] = 'o fim do arquivo';
LOCALE_PT$1['T_NUM'] = 'um número';
LOCALE_PT$1['T_STRING'] = 'uma corrente (string)';
LOCALE_PT$1['T_UPPERID'] = 'um identificador com maiúsculas';
LOCALE_PT$1['T_LOWERID'] = 'um identificador com minúsculas';
LOCALE_PT$1['T_PROGRAM'] = keyword$2('program');
LOCALE_PT$1['T_INTERACTIVE'] = keyword$2('interactive');
LOCALE_PT$1['T_PROCEDURE'] = keyword$2('procedure');
LOCALE_PT$1['T_FUNCTION'] = keyword$2('function');
LOCALE_PT$1['T_RETURN'] = keyword$2('return');
LOCALE_PT$1['T_IF'] = keyword$2('if');
LOCALE_PT$1['T_THEN'] = keyword$2('then');
LOCALE_PT$1['T_ELSE'] = keyword$2('else');
LOCALE_PT$1['T_REPEAT'] = keyword$2('repeat');
LOCALE_PT$1['T_FOREACH'] = keyword$2('foreach');
LOCALE_PT$1['T_IN'] = keyword$2('in');
LOCALE_PT$1['T_WHILE'] = keyword$2('while');
LOCALE_PT$1['T_SWITCH'] = keyword$2('switch');
LOCALE_PT$1['T_TO'] = keyword$2('to');
LOCALE_PT$1['T_LET'] = keyword$2('let');
LOCALE_PT$1['T_NOT'] = keyword$2('not');
LOCALE_PT$1['T_DIV'] = keyword$2('div');
LOCALE_PT$1['T_MOD'] = keyword$2('mod');
LOCALE_PT$1['T_TYPE'] = keyword$2('type');
LOCALE_PT$1['T_IS'] = keyword$2('is');
LOCALE_PT$1['T_RECORD'] = keyword$2('record');
LOCALE_PT$1['T_VARIANT'] = keyword$2('variant');
LOCALE_PT$1['T_CASE'] = keyword$2('case');
LOCALE_PT$1['T_FIELD'] = keyword$2('field');
LOCALE_PT$1['T_UNDERSCORE'] = 'um sublinhado ("_")';
LOCALE_PT$1['T_LPAREN'] = 'um parênteses esquerdo ("(")';
LOCALE_PT$1['T_RPAREN'] = 'um parênteses direito (")")';
LOCALE_PT$1['T_LBRACE'] = 'uma chave esquerda ("{")';
LOCALE_PT$1['T_RBRACE'] = 'uma chave direita ("}")';
LOCALE_PT$1['T_LBRACK'] = 'um colchete esquerdo ("[")';
LOCALE_PT$1['T_RBRACK'] = 'um colchete direito ("]")';
LOCALE_PT$1['T_COMMA'] = 'uma vírgula  (",")';
LOCALE_PT$1['T_SEMICOLON'] = 'um ponto e vírgula (";")';
LOCALE_PT$1['T_RANGE'] = 'um separador de intervalo ("..")';
LOCALE_PT$1['T_GETS'] = 'uma flecha para a esquerda ("<-")';
LOCALE_PT$1['T_PIPE'] = 'uma barra vertical ("|")';
LOCALE_PT$1['T_ARROW'] = 'uma flecha ("->")';
LOCALE_PT$1['T_ASSIGN'] = 'um operador de designação  (":=")';
LOCALE_PT$1['T_EQ'] = 'uma comparação por igualdade ("==")';
LOCALE_PT$1['T_NE'] = 'uma comparação por desigualdade ("/=")';
LOCALE_PT$1['T_LE'] = 'um menor ou igual ("<=")';
LOCALE_PT$1['T_GE'] = 'um maior ou igual (">=")';
LOCALE_PT$1['T_LT'] = 'um menor estrito ("<")';
LOCALE_PT$1['T_GT'] = 'um maior estrito (">")';
LOCALE_PT$1['T_AND'] = 'o "e" lógico ("&&")';
LOCALE_PT$1['T_OR'] = 'o "ou" lógico ("||")';
LOCALE_PT$1['T_CONCAT'] = 'o operador de concatenação de listas ("++")';
LOCALE_PT$1['T_PLUS'] = 'o operador de soma ("+")';
LOCALE_PT$1['T_MINUS'] = 'o operador de diferença ("-")';
LOCALE_PT$1['T_TIMES'] = 'o operador de produto ("*")';
LOCALE_PT$1['T_POW'] = 'o operador de potência ("^")';
/* Local name categories */
LOCALE_PT$1['LocalVariable'] = 'variável';
LOCALE_PT$1['LocalIndex'] = 'índice';
LOCALE_PT$1['LocalParameter'] = 'parâmetro';
/* Descriptions of value types */
LOCALE_PT$1['V_Integer'] = 'um número';
LOCALE_PT$1['V_String'] = 'uma cadeia';
LOCALE_PT$1['V_Tuple'] = 'uma tupla';
LOCALE_PT$1['V_List'] = 'uma lista';
LOCALE_PT$1['V_Structure'] = 'uma estrutura';
/* Lexer */
LOCALE_PT$1['errmsg:unclosed-multiline-comment'] = 'O comentário abre mas nunca fecha.';
LOCALE_PT$1['errmsg:unclosed-string-constant'] =
    'As aspas que abrem não possuem as aspas correspondentes que fecham.';
LOCALE_PT$1['errmsg:numeric-constant-should-not-have-leading-zeroes'] = `As constantes numéricas não podem ser escritas com zeros à esquerda.`;
LOCALE_PT$1['errmsg:identifier-must-start-with-alphabetic-character'] = `Os identificadores devem começar com um caractere alfabético (a...z,A...Z).`;
LOCALE_PT$1['errmsg:unknown-token'] = (symbol) => `Símbolo desconhecido na entrada: "${symbol}".`;
LOCALE_PT$1['warning:empty-pragma'] = 'Diretiva pragma vazia.';
LOCALE_PT$1['warning:unknown-pragma'] = (pragmaName) => 'Diretiva pragma desconhecida: "' + pragmaName + '".';
/* Parser */
LOCALE_PT$1['errmsg:empty-source'] = 'O programa está vazio.';
LOCALE_PT$1['errmsg:expected-but-found'] = (expected, found) => `Esperava-se ${expected}.
Encontrado: ${found}.`;
LOCALE_PT$1['errmsg:pattern-number-cannot-be-negative-zero'] = 'O padrão numérico não pode ser "-0".';
LOCALE_PT$1['errmsg:pattern-tuple-cannot-be-singleton'] =
    'O padrão para uma tupla não pode ter apenas um componente. ' +
        'As tuplas têm 0, 2, 3, ou mais componentes, mas não 1.';
LOCALE_PT$1['errmsg:assignment-tuple-cannot-be-singleton'] =
    'A designação a uma tupla não pode ser ' +
        ' constituída por apenas um componente. ' +
        'As tuplas têm 0, 2, 3, ou mais componentes, mas não 1.';
LOCALE_PT$1['errmsg:operators-are-not-associative'] = (op1, op2) => 'A expressão usa ' +
    op1 +
    ' e ' +
    op2 +
    ', mas estes operadores não podem ser associados. ' +
    'Talvez faltam parênteses.';
LOCALE_PT$1['errmsg:obsolete-tuple-assignment'] =
    'Esperava-se um comando mas não foi encontrado um parênteses esquerdo. ' +
        'Nota: a sintaxe de designação de tuplas "(x1, ..., xN) := y" ' +
        'está obsoleta. Usar "let (x1, ..., xN) := y".';
/* Linter */
LOCALE_PT$1['errmsg:program-already-defined'] = (pos1, pos2) => 'Já havia um programa definido em ' +
    pos1 +
    '.\n' +
    'Não é possível definir um programa em ' +
    pos2 +
    '.';
LOCALE_PT$1['errmsg:procedure-already-defined'] = (name, pos1, pos2) => 'O procedimiento "' +
    name +
    '" está definido duas vezes: ' +
    'em ' +
    pos1 +
    ' e em ' +
    pos2 +
    '.';
LOCALE_PT$1['errmsg:function-already-defined'] = (name, pos1, pos2) => `A função "${name}" está definida duas vezes: em ${pos1} e em ${pos2}.`;
LOCALE_PT$1['errmsg:type-already-defined'] = (name, pos1, pos2) => `O tipo "${name}" está definido duas vezes: em ${pos1} e em ${pos2}.`;
LOCALE_PT$1['errmsg:constructor-already-defined'] = (name, pos1, pos2) => `O construtor "${name}" está definido duas vezes: em ${pos1} e em ${pos2}.`;
LOCALE_PT$1['errmsg:repeated-field-name'] = (constructorName, fieldName) => 'O campo "' +
    fieldName +
    '" não pode estar repetido ' +
    'para o construtor "' +
    constructorName +
    '".';
LOCALE_PT$1['errmsg:function-and-field-cannot-have-the-same-name'] = (name, posFunction, posField) => 'O nome "' +
    name +
    '" usa-se ' +
    'para uma função em ' +
    posFunction +
    ' e ' +
    'para um campo em ' +
    posField +
    '.';
LOCALE_PT$1['errmsg:source-should-have-a-program-definition'] =
    /* Note: the code may actually be completely empty, but
     * we avoid this technicality since the message could be
     * confusing. */
    'O código deve ter uma definição de "program { ... }".';
LOCALE_PT$1['errmsg:procedure-should-not-have-return'] = (name) => `O procedimento "${name}" não deveria ter um comando "return".`;
LOCALE_PT$1['errmsg:function-should-have-return'] = (name) => 'A função "' + name + '" deveria ter um comando "return".';
LOCALE_PT$1['errmsg:return-statement-not-allowed-here'] =
    'O comando "return"  pode aparecer apenas como o último comando ' +
        'de uma função ou como o último comando do programa.';
LOCALE_PT$1['errmsg:local-name-conflict'] = (name, oldCat, oldPos, newCat, newPos) => 'Conflito de nomes: "' +
    name +
    '" se usa duas vezes: ' +
    'como ' +
    oldCat +
    ' em ' +
    oldPos +
    ', e ' +
    'como ' +
    newCat +
    ' em ' +
    newPos +
    '.';
LOCALE_PT$1['errmsg:repeated-variable-in-tuple-assignment'] = (name) => `La variável "${name}" está repetida na designação de tuplas.`;
LOCALE_PT$1['errmsg:constructor-used-as-procedure'] = (name, type) => 'O procedimento "' +
    name +
    '" não está definido. ' +
    'O nome "' +
    name +
    '" é o nome de um construtor ' +
    'do tipo "' +
    type +
    '".';
LOCALE_PT$1['errmsg:undefined-procedure'] = (name) => 'O procedimento "' + name + '" não está definido.';
LOCALE_PT$1['errmsg:undefined-function'] = (name) => 'A função "' + name + '" não está definida.';
LOCALE_PT$1['errmsg:procedure-arity-mismatch'] = (name, expected, received) => 'O procedimento "' +
    name +
    '" espera receber ' +
    toFunc$1$1(LOCALE_ES$1['<n>-parameters'])(expected) +
    ' mas é invocado com ' +
    toFunc$1$1(LOCALE_ES$1['<n>-arguments'])(received) +
    '.';
LOCALE_PT$1['errmsg:function-arity-mismatch'] = (name, expected, received) => 'A função "' +
    name +
    '" espera receber ' +
    toFunc$1$1(LOCALE_ES$1['<n>-parameters'])(expected) +
    ' mas é invocado com ' +
    toFunc$1$1(LOCALE_ES$1['<n>-arguments'])(received) +
    '.';
LOCALE_PT$1['errmsg:structure-pattern-arity-mismatch'] = (name, expected, received) => 'O construtor "' +
    name +
    '" tem ' +
    toFunc$1$1(LOCALE_ES$1['<n>-fields'])(expected) +
    ' mas o padrão tem ' +
    toFunc$1$1(LOCALE_ES$1['<n>-parameters'])(received) +
    '.';
LOCALE_PT$1['errmsg:type-used-as-constructor'] = (name, constructorNames) => {
    let msg;
    if (constructorNames.length === 0) {
        msg = '(não tem construtores).';
    }
    else if (constructorNames.length === 1) {
        msg = '(tem um construtor: ' + constructorNames[0] + ').';
    }
    else {
        msg = '(seus construtores são: ' + constructorNames.join(', ') + ').';
    }
    return ('O construtor "' +
        name +
        '" não está definido. ' +
        'O nome "' +
        name +
        '" é o nome de um tipo ' +
        msg);
};
LOCALE_PT$1['errmsg:procedure-used-as-constructor'] = (name) => 'O construtor "' +
    name +
    '" não está definido. ' +
    'O nome "' +
    name +
    '" é o nome de um procedimento.';
LOCALE_PT$1['errmsg:undeclared-constructor'] = (name) => 'O construtor "' + name + '" não está definido.';
LOCALE_PT$1['errmsg:wildcard-pattern-should-be-last'] =
    'O comodín "_" tem que ser o último ramo do switch.';
LOCALE_PT$1['errmsg:numeric-pattern-repeats-number'] = (number) => 'Tem dois ramos diferentes para o número "' + number + '".';
LOCALE_PT$1['errmsg:structure-pattern-repeats-constructor'] = (name) => 'Há dois ramos distintos para o construtor "' + name + '".';
LOCALE_PT$1['errmsg:structure-pattern-repeats-tuple-arity'] = (arity) => 'Há dois ramos distintos para as tuplas de ' + arity.toString() + ' componentes.';
LOCALE_PT$1['errmsg:structure-pattern-repeats-timeout'] = 'Há dois ramos distintos para o TIMEOUT.';
LOCALE_PT$1['errmsg:pattern-does-not-match-type'] = (expectedType, patternType) => 'Os padrões devem ser todos do mesmo tipo. ' +
    'O padrão deveria ser de tipo "' +
    expectedType +
    '" ' +
    'pero es de tipo "' +
    patternType +
    '".';
LOCALE_PT$1['errmsg:patterns-in-interactive-program-must-be-events'] =
    'Os padrões de um "interactive program" devem ser eventos.';
LOCALE_PT$1['errmsg:patterns-in-switch-must-not-be-events'] =
    'Os padrões de um "switch" não podem ser eventos.';
LOCALE_PT$1['errmsg:structure-construction-repeated-field'] = (constructorName, fieldName) => 'O campo "' +
    fieldName +
    '" está repetido em ' +
    'a instanciação do construtor "' +
    constructorName +
    '".';
LOCALE_PT$1['errmsg:structure-construction-invalid-field'] = (constructorName, fieldName) => 'O campo "' +
    fieldName +
    '" não é um campo válido ' +
    'para o construtor "' +
    constructorName +
    '".';
LOCALE_PT$1['errmsg:structure-construction-missing-field'] = (constructorName, fieldName) => `Falta dar valor ao campo "${fieldName}" do construtor "${constructorName}".`;
LOCALE_PT$1['errmsg:structure-construction-cannot-be-an-event'] = (constructorName) => 'O construtor "' +
    constructorName +
    '" corresponde a um ' +
    'evento, e só pode ser administrado implicitamente ' +
    'em um programa interativo (o usuário não pode construir ' +
    'instâncias).';
/* Runtime errors (virtual machine) */
LOCALE_PT$1['errmsg:undefined-variable'] = (variableName) => 'A variável "' + variableName + '" não está definida.';
LOCALE_PT$1['errmsg:too-few-arguments'] = (routineName) => 'Faltam argumentos para "' + routineName + '".';
LOCALE_PT$1['errmsg:expected-structure-but-got'] = (constructorName, valueTag) => 'Esperava-se uma estrutura construída ' +
    'com o construtor "' +
    constructorName +
    '", ' +
    'mas foi recebido ' +
    valueTag +
    '.';
LOCALE_PT$1['errmsg:expected-constructor-but-got'] = (constructorNameExpected, constructorNameReceived) => 'Esperava-se uma estrutura construída ' +
    'com o construtor "' +
    constructorNameExpected +
    '", ' +
    'mas o construtor recebido é ' +
    constructorNameReceived +
    '".';
LOCALE_PT$1['errmsg:incompatible-types-on-assignment'] = (variableName, oldType, newType) => 'A variável "' +
    variableName +
    '" ' +
    'continha un valor do tipo ' +
    oldType +
    ', ' +
    'não é possível designar um valor de tipo ' +
    newType +
    '".';
LOCALE_PT$1['errmsg:incompatible-types-on-list-creation'] = (index, oldType, newType) => 'Todos os elementos de uma lista devem ser do mesmo tipo. ' +
    'Os elementos são do tipo ' +
    oldType +
    ', ' +
    'mas o elemento na posição ' +
    index.toString() +
    ' ' +
    'é do tipo ' +
    newType +
    '.';
LOCALE_PT$1['errmsg:incompatible-types-on-structure-update'] = (fieldName, oldType, newType) => 'O campo "' +
    fieldName +
    '" é do tipo ' +
    oldType +
    '. ' +
    'Não pode ser atualizado com um valor do tipo ' +
    newType +
    '.';
LOCALE_PT$1['errmsg:expected-tuple-value-but-got'] = (receivedType) => `Esperava-se uma tupla mas um valor não foi recebido de tipo ${receivedType}.`;
LOCALE_PT$1['errmsg:tuple-component-out-of-bounds'] = (size, index) => 'Índice fora do intervalo. ' +
    'A tupla é do tamanho ' +
    size.toString() +
    ' e ' +
    'o índice é ' +
    index.toString() +
    '.';
LOCALE_PT$1['errmsg:expected-structure-value-but-got'] = (receivedType) => `Se esperaba una estructura pero se recibió un valor de tipo ${receivedType}.`;
LOCALE_PT$1['errmsg:structure-field-not-present'] = (fieldNames, missingFieldName) => 'A estrutura não possui um campo "' +
    missingFieldName +
    '". ' +
    'Os campos são: [' +
    fieldNames.join(', ') +
    '].';
LOCALE_PT$1['errmsg:primitive-does-not-exist'] = (primitiveName) => `A operação primitiva "${primitiveName}" não existe ou não está disponível.`;
LOCALE_PT$1['errmsg:primitive-arity-mismatch'] = (name, expected, received) => 'A operação "' +
    name +
    '" espera receber ' +
    toFunc$1$1(LOCALE_ES$1['<n>-parameters'])(expected) +
    ' mas é invocada com ' +
    toFunc$1$1(LOCALE_ES$1['<n>-arguments'])(received) +
    '.';
LOCALE_PT$1['errmsg:primitive-argument-type-mismatch'] = (name, parameterIndex, expectedType, receivedType) => 'O parâmetro #' +
    parameterIndex.toString() +
    ' ' +
    'da operação "' +
    name +
    '" ' +
    'deveria ser do tipo ' +
    expectedType +
    ' ' +
    'mas o argumento é do tipo ' +
    receivedType +
    '.';
LOCALE_PT$1['errmsg:expected-value-of-type-but-got'] = (expectedType, receivedType) => 'Esperava-se um valor do tipo ' +
    expectedType +
    ' ' +
    'mas foi recebido um valor do tipo ' +
    receivedType +
    '.';
LOCALE_PT$1['errmsg:expected-value-of-some-type-but-got'] = (expectedTypes, receivedType) => 'Esperava-se um valor de algum dos seguintes tipos: ' +
    expectedTypes.join(', ') +
    '; mas foi recebido um valor do tipo ' +
    receivedType +
    '.';
LOCALE_PT$1['errmsg:expected-values-to-have-compatible-types'] = (type1, type2) => 'Os tipos dos valores devem ser compatíveis, ' +
    'mas um é do tipo ' +
    type1 +
    ' ' +
    'e o outro é do tipo ' +
    type2 +
    '.';
LOCALE_PT$1['errmsg:switch-does-not-match'] =
    'O valor analisado não coincide com nenhum dos ramos do switch.';
LOCALE_PT$1['errmsg:cannot-divide-by-zero'] = 'Não é possível dividir por zero.';
LOCALE_PT$1['errmsg:list-cannot-be-empty'] = 'A lista não pode ser vazia.';
LOCALE_PT$1['errmsg:timeout'] = (millisecs) => 'A execução do programa demorou mais de ' + millisecs.toString() + 'ms.';
/* Board operations */
LOCALE_PT$1['errmsg:cannot-move-to'] = (dirName) => 'Não é possível mover para a direção ' + dirName + ': cai fora do tabuleiro.';
LOCALE_PT$1['errmsg:cannot-remove-stone'] = (dirName) => 'Não é posível retirar uma pedra de cor ' + dirName + ': não há pedras dessa cor.';
/* Runtime */
LOCALE_PT$1['TYPE:Color'] = 'Cor';
LOCALE_PT$1['CONS:Color0'] = 'Azul';
LOCALE_PT$1['CONS:Color1'] = 'Preto';
LOCALE_PT$1['CONS:Color2'] = 'Vermelho';
LOCALE_PT$1['CONS:Color3'] = 'Verde';
LOCALE_PT$1['TYPE:Dir'] = 'Dir';
LOCALE_PT$1['CONS:Dir0'] = 'Norte';
LOCALE_PT$1['CONS:Dir1'] = 'Leste';
LOCALE_PT$1['CONS:Dir2'] = 'Sul';
LOCALE_PT$1['CONS:Dir3'] = 'Oeste';
LOCALE_PT$1['PRIM:PutStone'] = 'Colocar';
LOCALE_PT$1['PRIM:RemoveStone'] = 'Retirar';
LOCALE_PT$1['PRIM:Move'] = 'Mover';
LOCALE_PT$1['PRIM:GoToEdge'] = 'IrABorda';
LOCALE_PT$1['PRIM:EmptyBoardContents'] = 'EsvaziarTabuleiro';
LOCALE_PT$1['PRIM:numStones'] = 'nroPedras';
LOCALE_PT$1['PRIM:anyStones'] = 'haPedras';
LOCALE_PT$1['PRIM:canMove'] = 'podeMover';
LOCALE_PT$1['PRIM:next'] = 'seguinte';
LOCALE_PT$1['PRIM:prev'] = 'previo';
LOCALE_PT$1['PRIM:opposite'] = 'oposto';
LOCALE_PT$1['PRIM:minBool'] = 'minBool';
LOCALE_PT$1['PRIM:maxBool'] = 'maxBool';
LOCALE_PT$1['PRIM:minColor'] = 'minCor';
LOCALE_PT$1['PRIM:maxColor'] = 'maxCor';
LOCALE_PT$1['PRIM:minDir'] = 'minDir';
LOCALE_PT$1['PRIM:maxDir'] = 'maxDir';
LOCALE_PT$1['PRIM:head'] = 'primeiro';
LOCALE_PT$1['PRIM:tail'] = 'resto';
LOCALE_PT$1['PRIM:oldTail'] = 'resto';
LOCALE_PT$1['PRIM:init'] = 'comeco';
LOCALE_PT$1['PRIM:last'] = 'ultimo';
/* Helpers */
LOCALE_PT$1['<alternative>'] = (strings) => 'alguma das seguintes alternativas:\n' + strings.map((s) => '  ' + s).join('\n');
LOCALE_PT$1['<position>'] = (filename, line, column) => filename + ':' + line.toString() + ':' + column.toString();
LOCALE_PT$1['<n>-parameters'] = (n) => pluralize$2(n, 'parâmetro', 'parâmetros');
LOCALE_PT$1['<n>-arguments'] = (n) => pluralize$2(n, 'argumento', 'argumentos');
LOCALE_PT$1['<n>-fields'] = (n) => pluralize$2(n, 'campo', 'campos');
LOCALE_PT$1['<pattern-type>'] = (patternType) => {
    if (patternType === 'Event') {
        return 'evento do programa interativo';
    }
    else if (patternType.substring(0, 7) === '_TUPLE_') {
        return 'tupla de ' + patternType.substring(7) + ' componentes';
    }
    else {
        return patternType;
    }
};

let CURRENT_LANGUAGE$1 = 'es';
const dictionaries$1 = {
    es: LOCALE_ES$1,
    en: LOCALE_EN$1,
    pt: LOCALE_PT$1
};
const i18n$1 = (message) => dictionaries$1[CURRENT_LANGUAGE$1][message];
const i18nF = (message) => dictionaries$1[CURRENT_LANGUAGE$1][message];
const i18nPosition = (position) => {
    const msg = i18nF('<position>');
    if (typeof msg === 'string')
        return msg;
    return msg(position.filename, position.line, position.column);
};

/* Base class for signalling conditions */
class GbsInterpreterException extends Error {
    /* Note: position should typically be an instance of SourceReader */
    constructor(startPos, endPos, errorType, reason, args) {
        super(reason);
        this.isGobstonesException = true;
        this.startPos = startPos;
        this.endPos = endPos;
        this.reason = reason;
        this.args = args;
        const errmsg = i18n$1(errorType + ':' + reason);
        const msg = typeof errmsg === 'string' || errmsg === undefined
            ? errmsg
            : // eslint-disable-next-line @typescript-eslint/ban-types
                errmsg(...args);
        this.message = reason === 'boom-called' ? args[0] : msg;
    }
}
class GbsWarning extends GbsInterpreterException {
    constructor(startPos, endPos, reason, args) {
        super(startPos, endPos, 'warning', reason, args);
    }
}
class GbsSyntaxError extends GbsInterpreterException {
    constructor(startPos, endPos, reason, args) {
        super(startPos, endPos, 'errmsg', reason, args);
    }
}
class GbsRuntimeError extends GbsInterpreterException {
    constructor(startPos, endPos, reason, args) {
        super(startPos, endPos, 'errmsg', reason, args);
    }
}

/* eslint-disable no-underscore-dangle */
/* Description of a field */
class FieldDescriptor {
    constructor(typeName, constructorName, index) {
        this._typeName = typeName;
        this._constructorName = constructorName;
        this._index = index;
    }
    get typeName() {
        return this._typeName;
    }
    get constructorName() {
        return this._constructorName;
    }
    get index() {
        return this._index;
    }
}
/* Local name categories */
const LocalVariable = Symbol.for('LocalVariable');
const LocalParameter = Symbol.for('LocalParameter');
const LocalIndex = Symbol.for('LocalIndex');
/* Description of a local name */
class LocalNameDescriptor {
    constructor(category, position) {
        this._category = category;
        this._position = position;
    }
    // eslint-disable-next-line @typescript-eslint/explicit-function-return-type
    get category() {
        return this._category;
    }
    // eslint-disable-next-line @typescript-eslint/explicit-function-return-type
    get position() {
        return this._position;
    }
}
function fail$3(startPos, endPos, reason, args) {
    throw new GbsSyntaxError(startPos, endPos, reason, args);
}
/* A symbol table keeps track of definitions, associating:
 * - procedure and function names to their code
 * - type definitions, constructors, and fields
 */
class SymbolTable {
    constructor() {
        this._program = undefined;
        /* true iff the program is interactive */
        this._isInteractiveProgram = false;
        /* Each procedure name is mapped to its definition */
        this._procedures = {};
        /* Each procedure name is mapped to its parameters */
        this._procedureParameters = {};
        /* Each function name is mapped to its definition */
        this._functions = {};
        /* Each function name is mapped to its parameters */
        this._functionParameters = {};
        /* Each type name is mapped to its definition */
        this._types = {};
        /* Each type name is mapped to a list of constructor names */
        this._typeConstructors = {};
        /* Each constructor name is mapped to its declaration */
        this._constructors = {};
        /* Each constructor name is mapped to its type name */
        this._constructorType = {};
        /* Each constructor name is mapped to a list of field names */
        this._constructorFields = {};
        /* Each field name is mapped to a list of field descriptors.
         * Each field descriptor is of the form
         *   new FieldDescriptor(typeName, constructorName, index)
         * where
         * - 'typeName' is the name of a type
         * - 'constructorName' is the name of a constructor of the given type
         * - 'index' is the index of the given field with respect to the
         *   given constructor (starting from 0)
         */
        this._fields = {};
        /* Local names include parameters, indices and variables,
         * which are only meaningful within a routine.
         *
         * Local names may be bound/referenced in the following places:
         * - formal parameters,
         * - indices of a "foreach",
         * - pattern matching (formal parameters of a "switch"),
         * - assignments and tuple assignments,
         * - reading local variables.
         *
         * _localNames maps a name to a descriptor of the form:
         *   new LocalNameDescriptor(category, position)
         */
        this._localNames = {};
    }
    get program() {
        return this._program;
    }
    isInteractiveProgram() {
        return this._isInteractiveProgram;
    }
    isProcedure(name) {
        return name in this._procedures;
    }
    allProcedureNames() {
        const names = [];
        for (const name in this._procedures) {
            names.push(name);
        }
        return names.sort();
    }
    procedureDefinition(name) {
        if (this.isProcedure(name)) {
            return this._procedures[name];
        }
        else {
            throw Error('Undefined procedure.');
        }
    }
    procedureParameters(name) {
        if (this.isProcedure(name)) {
            return this._procedureParameters[name];
        }
        else {
            throw Error('Undefined procedure.');
        }
    }
    isFunction(name) {
        return name in this._functions;
    }
    allFunctionNames() {
        const names = [];
        for (const name in this._functions) {
            names.push(name);
        }
        return names.sort();
    }
    functionDefinition(name) {
        if (this.isFunction(name)) {
            return this._functions[name];
        }
        else {
            throw Error('Undefined function.');
        }
    }
    functionParameters(name) {
        if (this.isFunction(name)) {
            return this._functionParameters[name];
        }
        else {
            throw Error('Undefined function.');
        }
    }
    isType(name) {
        return name in this._types;
    }
    typeDefinition(name) {
        if (this.isType(name)) {
            return this._types[name];
        }
        else {
            throw Error('Undefined type.');
        }
    }
    typeConstructors(name) {
        if (this.isType(name)) {
            return this._typeConstructors[name];
        }
        else {
            throw Error('Undefined type.');
        }
    }
    isConstructor(name) {
        return name in this._constructors;
    }
    constructorDeclaration(name) {
        if (this.isConstructor(name)) {
            return this._constructors[name];
        }
        else {
            throw Error('Undefined constructor.');
        }
    }
    constructorType(name) {
        if (this.isConstructor(name)) {
            return this._constructorType[name];
        }
        else {
            throw Error('Undefined constructor.');
        }
    }
    constructorFields(name) {
        if (this.isConstructor(name)) {
            return this._constructorFields[name];
        }
        else {
            throw Error('Undefined constructor.');
        }
    }
    isField(name) {
        return name in this._fields;
    }
    fieldDescriptor(name) {
        if (this.isField(name)) {
            return this._fields[name];
        }
        else {
            throw Error('Undefined field.');
        }
    }
    defProgram(definition) {
        if (this._program !== undefined) {
            fail$3(definition.startPos, definition.endPos, 'program-already-defined', [
                i18nPosition(this._program.startPos),
                i18nPosition(definition.startPos)
            ]);
        }
        this._program = definition;
    }
    defInteractiveProgram(definition) {
        this.defProgram(definition);
        this._isInteractiveProgram = true;
    }
    defProcedure(definition) {
        const name = definition.name.value;
        if (name in this._procedures) {
            fail$3(definition.name.startPos, definition.name.endPos, 'procedure-already-defined', [
                name,
                i18nPosition(this._procedures[name].startPos),
                i18nPosition(definition.startPos)
            ]);
        }
        const parameters = [];
        for (const parameter of definition.parameters) {
            parameters.push(parameter.value);
        }
        this._procedures[name] = definition;
        this._procedureParameters[name] = parameters;
    }
    defFunction(definition) {
        const name = definition.name.value;
        if (name in this._functions) {
            fail$3(definition.name.startPos, definition.name.endPos, 'function-already-defined', [
                name,
                i18nPosition(this._functions[name].startPos),
                i18nPosition(definition.startPos)
            ]);
        }
        else if (name in this._fields) {
            const fieldPos = this._constructors[this._fields[name][0].constructorName].startPos;
            fail$3(definition.name.startPos, definition.name.endPos, 'function-and-field-cannot-have-the-same-name', [name, i18nPosition(definition.startPos), i18nPosition(fieldPos)]);
        }
        const parameters = [];
        for (const parameter of definition.parameters) {
            parameters.push(parameter.value);
        }
        this._functions[name] = definition;
        this._functionParameters[name] = parameters;
    }
    defType(definition) {
        const typeName = definition.typeName.value;
        if (typeName in this._types) {
            fail$3(definition.typeName.startPos, definition.typeName.endPos, 'type-already-defined', [
                typeName,
                i18nPosition(this._types[typeName].startPos),
                i18nPosition(definition.startPos)
            ]);
        }
        this._types[typeName] = definition;
        const constructorNames = [];
        for (const constructorDeclaration of definition.constructorDeclarations) {
            this._declareConstructor(typeName, constructorDeclaration);
            constructorNames.push(constructorDeclaration.constructorName.value);
        }
        this._typeConstructors[typeName] = constructorNames;
    }
    _declareConstructor(typeName, constructorDeclaration) {
        const constructorName = constructorDeclaration.constructorName.value;
        if (constructorName in this._constructors) {
            fail$3(constructorDeclaration.constructorName.startPos, constructorDeclaration.constructorName.endPos, 'constructor-already-defined', [
                constructorName,
                i18nPosition(this._constructors[constructorName].startPos),
                i18nPosition(constructorDeclaration.startPos)
            ]);
        }
        this._constructors[constructorName] = constructorDeclaration;
        this._constructorType[constructorName] = typeName;
        const constructorFields = {};
        const fieldNames = [];
        let index = 0;
        for (const fieldName of constructorDeclaration.fieldNames) {
            if (fieldName.value in constructorFields) {
                fail$3(fieldName.startPos, fieldName.endPos, 'repeated-field-name', [
                    constructorName,
                    fieldName.value
                ]);
            }
            constructorFields[fieldName.value] = true;
            fieldNames.push(fieldName.value);
            this._declareField(fieldName.startPos, fieldName.endPos, typeName, constructorName, fieldName.value, index);
            index++;
        }
        this._constructorFields[constructorName] = fieldNames;
    }
    _declareField(startPos, endPos, typeName, constructorName, fieldName, index) {
        if (fieldName in this._functions) {
            fail$3(startPos, endPos, 'function-and-field-cannot-have-the-same-name', [
                fieldName,
                i18nPosition(this._functions[fieldName].startPos),
                i18nPosition(startPos)
            ]);
        }
        if (!(fieldName in this._fields)) {
            this._fields[fieldName] = [];
        }
        this._fields[fieldName].push(new FieldDescriptor(typeName, constructorName, index));
    }
    /* Adds a new local name, failing if it already exists. */
    addNewLocalName(localName, category) {
        if (localName.value in this._localNames) {
            fail$3(localName.startPos, localName.endPos, 'local-name-conflict', [
                localName.value,
                i18n$1(Symbol.keyFor(this._localNames[localName.value].category)),
                i18nPosition(this._localNames[localName.value].position),
                i18n$1(Symbol.keyFor(category)),
                i18nPosition(localName.startPos)
            ]);
        }
        this.setLocalName(localName, category);
    }
    /* Sets a local name.
     * It fails if it already exists with a different category. */
    setLocalName(localName, category) {
        if (localName.value in this._localNames &&
            this._localNames[localName.value].category !== category) {
            fail$3(localName.startPos, localName.endPos, 'local-name-conflict', [
                localName.value,
                i18n$1(Symbol.keyFor(this._localNames[localName.value].category)),
                i18nPosition(this._localNames[localName.value].position),
                i18n$1(Symbol.keyFor(category)),
                i18nPosition(localName.startPos)
            ]);
        }
        this._localNames[localName.value] = new LocalNameDescriptor(category, localName.startPos);
    }
    /* Removes a local name. */
    removeLocalName(localName) {
        delete this._localNames[localName.value];
    }
    /* Removes all local names. */
    exitScope() {
        this._localNames = {};
    }
    /* Get the attribute dictionary for a global name.
     *
     * A global name is the names of a global definition:
     *   - the string 'program'
     *   - any procedure name (e.g. 'P')
     *   - any function name (e.g. 'f')
     *   - any type name (e.g. 'A')
     *
     * The result is a dictionary of attributes.
     *
     */
    getAttributes(globalName) {
        if (globalName === 'program' && this._program !== undefined) {
            return this._program.attributes;
        }
        else if (globalName in this._procedures) {
            return this._procedures[globalName].attributes;
        }
        else if (globalName in this._functions) {
            return this._functions[globalName].attributes;
        }
        else if (globalName in this._types) {
            return this._types[globalName].attributes;
        }
        else {
            return {};
        }
    }
}

/* eslint-disable camelcase */
class RecursionChecker {
    constructor() {
        this._callGraph = {};
    }
    /*
     * If there is a cycle in the call graph (using either procedure calls
     * or function calls), return a list:
     *   [c1, ..., cn]
     * where ci is the i-th call involved in a cycle.
     * A call is of the form:
     *   {caller: F , callee: G, location: L}
     * where F is the name (string) of the caller,
     *       G is the name (string) of the callee,
     *   and L is the location of the call.
     *
     * Otherwise return null.
     */
    callCycle(ast) {
        /* Build the call graph */
        this._visitNode(ast);
        /* Find a cycle in the call graph */
        return this._findCallCycle();
    }
    /* Visitor -- build the call graph */
    _addEdge(caller, callee) {
        if (!(caller in this._callGraph)) {
            this._callGraph[caller] = {};
        }
        if (!(callee.value in this._callGraph[caller])) {
            this._callGraph[caller][callee.value] = callee;
        }
    }
    _visitNode(node) {
        if (node === undefined || node instanceof Token) ;
        else if (node instanceof Array) {
            this._visitNodes(node);
        }
        else {
            this._visitTaggedNode(node);
        }
    }
    _visitNodes(nodes) {
        for (const node of nodes) {
            this._visitNode(node);
        }
    }
    // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
    _visitTaggedNode(node) {
        switch (node.tag) {
            case N_DefProgram:
            case N_DefInteractiveProgram:
                this._visitProgramDefinition();
                break;
            case N_DefProcedure:
            case N_DefFunction:
                this._visitRoutineDefinition(node);
                break;
            case N_StmtProcedureCall:
                this._visitProcedureCall(node);
                break;
            case N_ExprFunctionCall:
                this._visitFunctionCall(node);
                break;
        }
        this._visitNodes(node.children);
    }
    _visitProgramDefinition() {
        this._currentRoutine = 'program';
    }
    _visitRoutineDefinition(node) {
        this._currentRoutine = node.name.value;
    }
    _visitProcedureCall(node) {
        this._addEdge(this._currentRoutine, node.procedureName);
    }
    _visitFunctionCall(node) {
        this._addEdge(this._currentRoutine, node.functionName);
    }
    /* Find a cycle in the call graph */
    _findCallCycle() {
        const visited = {};
        const parents = {};
        for (const f in this._callGraph) {
            visited[f] = true;
            parents[f] = true;
            const cycle = this._findCallCycleFrom(visited, parents, [], f);
            if (cycle !== undefined) {
                return cycle;
            }
            delete parents[f];
        }
        return undefined;
    }
    _findCallCycleFrom(visited, parents, path, f) {
        for (const g in this._callGraph[f]) {
            path.push({
                caller: f,
                callee: g,
                location: this._callGraph[f][g]
            });
            if (g in parents) {
                while (path[0].caller !== g) {
                    path.shift();
                }
                path.push();
                return path; /* Cycle */
            }
            if (!(g in visited)) {
                visited[g] = true;
                parents[g] = true;
                const cycle = this._findCallCycleFrom(visited, parents, path, g);
                if (cycle !== undefined) {
                    return cycle;
                }
                delete parents[g];
            }
            path.pop();
        }
        return undefined;
    }
}

/* eslint-disable camelcase */
// Only for typing purposes
// eslint-disable-next-line @typescript-eslint/ban-types
const toStr$1 = (x) => x;
const isBlockWithReturn = (stmt) => stmt.tag === N_StmtBlock &&
    stmt.statements.length > 0 &&
    stmt.statements.slice(-1)[0].tag === N_StmtReturn;
function fail$2(startPos, endPos, reason, args) {
    throw new GbsSyntaxError(startPos, endPos, reason, args);
}
/* A semantic analyzer receives
 *   a symbol table (instance of SymbolTable)
 *   an abstract syntax tree (the output of a parser)
 *
 * Then:
 *
 * - It performs semantic checks (linting) to ensure that the
 *   program is well-formed.
 *
 * - It builds a symbol table with information on global identifiers
 *   such as procedures, functions, types, constructors, and fields.
 *
 * - The semantic analysis is structured as a recursive visit over the
 *   AST.
 *
 * We assume that the AST is the valid output of a parser.
 */
class Linter {
    constructor(symtable) {
        this._symtable = symtable;
        /* All checks performed by the linter have an entry in this dictionary.
         * The value of a check indicates whether it is enabled (true) or
         * disabled (false).
         *
         * If a check is disabled, it does not produce a syntax error.
         */
        this._enabledLinterChecks = {
            // Linter options
            'source-should-have-a-program-definition': true,
            'procedure-should-not-have-return': true,
            'function-should-have-return': true,
            'return-statement-not-allowed-here': true,
            'wildcard-pattern-should-be-last': true,
            'variable-pattern-should-be-last': true,
            'structure-pattern-repeats-constructor': true,
            'structure-pattern-repeats-tuple-arity': true,
            'structure-pattern-repeats-timeout': true,
            'pattern-does-not-match-type': true,
            'patterns-in-interactive-program-must-be-events': true,
            'patterns-in-interactive-program-cannot-be-variables': true,
            'patterns-in-switch-must-not-be-events': true,
            'patterns-in-foreach-must-not-be-events': true,
            'repeated-variable-in-tuple-assignment': true,
            'constructor-used-as-procedure': true,
            'undefined-procedure': true,
            'procedure-arity-mismatch': true,
            'numeric-pattern-repeats-number': true,
            'structure-pattern-arity-mismatch': true,
            'structure-construction-repeated-field': true,
            'structure-construction-invalid-field': true,
            'structure-construction-missing-field': true,
            'structure-construction-cannot-be-an-event': true,
            'undefined-function': true,
            'function-arity-mismatch': true,
            'type-used-as-constructor': true,
            'procedure-used-as-constructor': true,
            'undeclared-constructor': true,
            // Extensions
            'forbidden-extension-destructuring-foreach': true,
            'forbidden-extension-allow-recursion': true
        };
    }
    lint(ast) {
        this._lintMain(ast);
        return this._symtable;
    }
    _ensureLintCheckExists(linterCheckId) {
        if (!(linterCheckId in this._enabledLinterChecks)) {
            throw Error('Linter check "' + linterCheckId + '" does not exist.');
        }
    }
    enableCheck(linterCheckId, enabled) {
        this._ensureLintCheckExists(linterCheckId);
        this._enabledLinterChecks[linterCheckId] = enabled;
    }
    _lintCheck(startPos, endPos, reason, args) {
        this._ensureLintCheckExists(reason);
        if (this._enabledLinterChecks[reason]) {
            fail$2(startPos, endPos, reason, args);
        }
    }
    _lintMain(ast) {
        /* Collect all definitions into the symbol table.
         * This should be done all together, before linting individual
         * definitions, so all the names of types, constructors, fields, etc.
         * are already known when checking statements and expressions. */
        for (const definition of ast.definitions) {
            this._addDefinitionToSymbolTable(definition);
        }
        /* The source should either be empty or have exactly one program */
        if (ast.definitions.length > 0 && this._symtable.program === undefined) {
            this._lintCheck(ast.startPos, ast.endPos, 'source-should-have-a-program-definition', []);
        }
        /* Lint individual definitions */
        for (const definition of ast.definitions) {
            this._lintDefinition(definition);
        }
        /* Disable recursion */
        this._disableRecursion(ast);
    }
    // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
    _addDefinitionToSymbolTable(definition) {
        switch (definition.tag) {
            case N_DefProgram:
                return this._symtable.defProgram(definition);
            case N_DefInteractiveProgram:
                return this._symtable.defInteractiveProgram(definition);
            case N_DefProcedure:
                return this._symtable.defProcedure(definition);
            case N_DefFunction:
                return this._symtable.defFunction(definition);
            case N_DefType:
                return this._symtable.defType(definition);
            default:
                throw Error('Unknown definition: ' + Symbol.keyFor(definition.tag));
        }
    }
    /** Definitions **/
    _lintDefinition(definition) {
        switch (definition.tag) {
            case N_DefProgram:
                return this._lintDefProgram(definition);
            case N_DefInteractiveProgram:
                return this._lintDefInteractiveProgram(definition);
            case N_DefProcedure:
                return this._lintDefProcedure(definition);
            case N_DefFunction:
                return this._lintDefFunction(definition);
            case N_DefType:
                return this._lintDefType();
            default:
                throw Error('Linter: Definition not implemented: ' + Symbol.keyFor(definition.tag));
        }
    }
    _lintDefProgram(definition) {
        /* Lint body */
        this._lintStmtBlock(definition.body, true /* allowReturn */);
        /* Remove all local names */
        this._symtable.exitScope();
    }
    _lintDefInteractiveProgram(definition) {
        /* Lint all branches */
        this._lintSwitchBranches(definition.branches, true /* isInteractiveProgram */);
    }
    _lintDefProcedure(definition) {
        /* Check that it does not have a return statement */
        if (isBlockWithReturn(definition.body)) {
            this._lintCheck(definition.startPos, definition.endPos, 'procedure-should-not-have-return', [definition.name.value]);
        }
        /* Add parameters as local names */
        for (const parameter of definition.parameters) {
            this._symtable.addNewLocalName(parameter, LocalParameter);
        }
        /* Lint body */
        this._lintStmtBlock(definition.body, false /* !allowReturn */);
        /* Remove all local names */
        this._symtable.exitScope();
    }
    _lintDefFunction(definition) {
        /* Check that it has a return statement */
        if (!isBlockWithReturn(definition.body)) {
            this._lintCheck(definition.startPos, definition.endPos, 'function-should-have-return', [
                definition.name.value
            ]);
        }
        /* Add parameters as local names */
        for (const parameter of definition.parameters) {
            this._symtable.addNewLocalName(parameter, LocalParameter);
        }
        /* Lint body */
        this._lintStmtBlock(definition.body, true /* allowReturn */);
        /* Remove all local names */
        this._symtable.exitScope();
    }
    _lintDefType() {
        /* No restrictions */
    }
    /** Statements **/
    _lintStatement(statement) {
        switch (statement.tag) {
            case N_StmtBlock:
                /* Do not allow return in nested blocks */
                return this._lintStmtBlock(statement, false /* !allowReturn */);
            case N_StmtReturn:
                return this._lintStmtReturn(statement);
            case N_StmtIf:
                return this._lintStmtIf(statement);
            case N_StmtRepeat:
                return this._lintStmtRepeat(statement);
            case N_StmtForeach:
                return this._lintStmtForeach(statement);
            case N_StmtWhile:
                return this._lintStmtWhile(statement);
            case N_StmtSwitch:
                return this._lintStmtSwitch(statement);
            case N_StmtAssignVariable:
                return this._lintStmtAssignVariable(statement);
            case N_StmtAssignTuple:
                return this._lintStmtAssignTuple(statement);
            case N_StmtProcedureCall:
                return this._lintStmtProcedureCall(statement);
            default:
                throw Error('Linter: Statement not implemented: ' + Symbol.keyFor(statement.tag));
        }
    }
    _lintStmtBlock(block, allowReturn) {
        let i = 0;
        for (const statement of block.statements) {
            const returnAllowed = allowReturn && i === block.statements.length - 1;
            if (!returnAllowed && statement.tag === N_StmtReturn) {
                this._lintCheck(statement.startPos, statement.endPos, 'return-statement-not-allowed-here', []);
            }
            this._lintStatement(statement);
            i++;
        }
    }
    _lintStmtReturn(statement) {
        this._lintExpression(statement.result);
    }
    _lintStmtIf(statement) {
        this._lintExpression(statement.condition);
        this._lintStatement(statement.thenBlock);
        if (statement.elseBlock !== undefined) {
            this._lintStatement(statement.elseBlock);
        }
    }
    _lintStmtRepeat(statement) {
        this._lintExpression(statement.times);
        this._lintStatement(statement.body);
    }
    _lintStmtForeach(statement) {
        this._lintStmtForeachPattern(statement.pattern);
        this._lintExpression(statement.range);
        for (const variable of statement.pattern.boundVariables) {
            this._symtable.addNewLocalName(variable, LocalIndex);
        }
        this._lintStatement(statement.body);
        for (const variable of statement.pattern.boundVariables) {
            this._symtable.removeLocalName(variable);
        }
    }
    _lintStmtForeachPattern(pattern) {
        /* If "DestructuringForeach" is disabled, forbid complex patterns.
         * Allow only variable patterns (indices). */
        if (pattern.tag !== N_PatternVariable) {
            this._lintCheck(pattern.startPos, pattern.endPos, 'forbidden-extension-destructuring-foreach', []);
        }
        /* Check that the pattern itself is well-formed */
        this._lintPattern(pattern);
        /* The pattern in a foreach cannot be an event */
        const patternType = this._patternType(pattern);
        if (patternType === i18n$1('TYPE:Event')) {
            this._lintCheck(pattern.startPos, pattern.endPos, 'patterns-in-foreach-must-not-be-events', []);
        }
    }
    _lintStmtWhile(statement) {
        this._lintExpression(statement.condition);
        this._lintStatement(statement.body);
    }
    _lintStmtSwitch(statement) {
        this._lintExpression(statement.subject);
        this._lintSwitchBranches(statement.branches, false /* !isInteractiveProgram */);
    }
    _lintSwitchBranches(branches, isInteractiveProgram) {
        this._lintBranches(branches, isInteractiveProgram, false /* isMatching */);
    }
    _lintBranches(branches, isInteractiveProgram, isMatching) {
        /* Check that each pattern is well-formed */
        for (const branch of branches) {
            this._lintPattern(branch.pattern);
        }
        this._branchesCheckWildcardAndVariable(branches);
        this._branchesCheckNoRepeats(branches);
        this._branchesCheckCompatible(branches);
        if (isInteractiveProgram) {
            this._branchesCheckTypeEvent(branches);
        }
        else {
            this._branchesCheckTypeNotEvent(branches);
        }
        /* Lint recursively each branch */
        for (const branch of branches) {
            this._lintBranchBody(branch, isMatching);
        }
    }
    /* Check that there is at most one wildcard/variable pattern at the end */
    _branchesCheckWildcardAndVariable(branches) {
        let i = 0;
        const n = branches.length;
        for (const branch of branches) {
            if (branch.pattern.tag === N_PatternWildcard && i !== n - 1) {
                this._lintCheck(branch.pattern.startPos, branch.pattern.endPos, 'wildcard-pattern-should-be-last', []);
            }
            if (branch.pattern.tag === N_PatternVariable && i !== n - 1) {
                this._lintCheck(branch.pattern.startPos, branch.pattern.endPos, 'variable-pattern-should-be-last', [branch.pattern.variableName.value]);
            }
            i++;
        }
    }
    /* Check that there are no repeated constructors in a sequence
     * of branches. */
    _branchesCheckNoRepeats(branches) {
        const coveredNumbers = {};
        const coveredConstructors = {};
        const coveredTuples = {};
        let coveredTimeout = false;
        for (const branch of branches) {
            switch (branch.pattern.tag) {
                case N_PatternWildcard:
                case N_PatternVariable:
                    /* Already checked in _switchBranchesCheckWildcardAndVariable */
                    break;
                case N_PatternNumber: {
                    const number = branch.pattern.number.value;
                    if (number in coveredNumbers) {
                        this._lintCheck(branch.pattern.startPos, branch.pattern.endPos, 'numeric-pattern-repeats-number', [number]);
                    }
                    coveredNumbers[number] = true;
                    break;
                }
                case N_PatternStructure: {
                    const constructorName = branch.pattern.constructorName.value;
                    if (constructorName in coveredConstructors) {
                        this._lintCheck(branch.pattern.startPos, branch.pattern.endPos, 'structure-pattern-repeats-constructor', [constructorName]);
                    }
                    coveredConstructors[constructorName] = true;
                    break;
                }
                case N_PatternTuple: {
                    const arity = branch.pattern.boundVariables.length;
                    if (arity in coveredTuples) {
                        this._lintCheck(branch.pattern.startPos, branch.pattern.endPos, 'structure-pattern-repeats-tuple-arity', [arity]);
                    }
                    coveredTuples[arity] = true;
                    break;
                }
                case N_PatternTimeout: {
                    if (coveredTimeout) {
                        this._lintCheck(branch.pattern.startPos, branch.pattern.endPos, 'structure-pattern-repeats-timeout', []);
                    }
                    coveredTimeout = true;
                    break;
                }
                default:
                    throw Error('Linter: pattern "' +
                        Symbol.keyFor(branch.pattern.tag) +
                        '" not implemented.');
            }
        }
    }
    /* Check that constructors are compatible,
     * i.e. that they belong to the same type */
    _branchesCheckCompatible(branches) {
        let expectedType;
        for (const branch of branches) {
            const patternType = this._patternType(branch.pattern);
            if (expectedType === undefined) {
                expectedType = patternType;
            }
            else if (patternType !== undefined && expectedType !== patternType) {
                this._lintCheck(branch.pattern.startPos, branch.pattern.endPos, 'pattern-does-not-match-type', [i18nF('<pattern-type>')(expectedType), i18nF('<pattern-type>')(patternType)]);
            }
        }
    }
    /* Check that there are patterns are of type Event */
    _branchesCheckTypeEvent(branches) {
        for (const branch of branches) {
            const patternType = this._patternType(branch.pattern);
            if (patternType !== undefined && patternType !== i18n$1('TYPE:Event')) {
                this._lintCheck(branch.pattern.startPos, branch.pattern.endPos, 'patterns-in-interactive-program-must-be-events', []);
            }
            if (branch.pattern.tag === N_PatternVariable) {
                this._lintCheck(branch.pattern.startPos, branch.pattern.endPos, 'patterns-in-interactive-program-cannot-be-variables', []);
            }
        }
    }
    /* Check that there are no patterns of type Event */
    _branchesCheckTypeNotEvent(branches) {
        for (const branch of branches) {
            const patternType = this._patternType(branch.pattern);
            if (patternType === i18n$1('TYPE:Event')) {
                this._lintCheck(branch.pattern.startPos, branch.pattern.endPos, 'patterns-in-switch-must-not-be-events', []);
            }
        }
    }
    /* Recursively lint the body of each branch. Locally bind variables. */
    _lintBranchBody(branch, isMatching) {
        for (const variable of branch.pattern.boundVariables) {
            this._symtable.addNewLocalName(variable, LocalParameter);
        }
        if (isMatching) {
            this._lintExpression(branch.body);
        }
        else {
            this._lintStatement(branch.body);
        }
        for (const variable of branch.pattern.boundVariables) {
            this._symtable.removeLocalName(variable);
        }
    }
    /* Return a description of the type of a pattern */
    _patternType(pattern) {
        switch (pattern.tag) {
            case N_PatternWildcard:
            case N_PatternVariable:
                return undefined;
            case N_PatternNumber:
                return toStr$1(i18n$1('TYPE:Integer'));
            case N_PatternStructure:
                return this._symtable.constructorType(pattern.constructorName.value);
            case N_PatternTuple:
                return '_TUPLE_' + pattern.boundVariables.length.toString();
            case N_PatternTimeout:
                return toStr$1(i18n$1('TYPE:Event'));
            default:
                throw Error('Linter: pattern "' + Symbol.keyFor(pattern.tag) + '" not implemented.');
        }
    }
    _lintStmtAssignVariable(statement) {
        this._symtable.setLocalName(statement.variable, LocalVariable);
        this._lintExpression(statement.value);
    }
    _lintStmtAssignTuple(statement) {
        const variables = {};
        for (const variable of statement.variables) {
            this._symtable.setLocalName(variable, LocalVariable);
            if (variable.value in variables) {
                this._lintCheck(variable.startPos, variable.endPos, 'repeated-variable-in-tuple-assignment', [variable.value]);
            }
            variables[variable.value] = true;
        }
        this._lintExpression(statement.value);
    }
    _lintStmtProcedureCall(statement) {
        const name = statement.procedureName.value;
        /* Check that it is a procedure */
        if (!this._symtable.isProcedure(name)) {
            if (this._symtable.isConstructor(name)) {
                this._lintCheck(statement.startPos, statement.endPos, 'constructor-used-as-procedure', [name, this._symtable.constructorType(name)]);
            }
            else {
                this._lintCheck(statement.startPos, statement.endPos, 'undefined-procedure', [
                    name
                ]);
            }
        }
        /* Check that the number of argument coincides */
        const expected = this._symtable.procedureParameters(name).length;
        const received = statement.args.length;
        if (expected !== received) {
            this._lintCheck(statement.startPos, statement.endPos, 'procedure-arity-mismatch', [
                name,
                expected,
                received
            ]);
        }
        /* Check all the arguments */
        for (const argument of statement.args) {
            this._lintExpression(argument);
        }
    }
    /** Patterns **/
    _lintPattern(pattern) {
        switch (pattern.tag) {
            case N_PatternWildcard:
                return this._lintPatternWildcard();
            case N_PatternVariable:
                return this._lintPatternVariable();
            case N_PatternNumber:
                return this._lintPatternNumber();
            case N_PatternStructure:
                return this._lintPatternStructure(pattern);
            case N_PatternTuple:
                return this._lintPatternTuple();
            case N_PatternTimeout:
                return this._lintPatternTimeout();
            default:
                throw Error('Linter: pattern "' + Symbol.keyFor(pattern.tag) + '" not implemented.');
        }
    }
    _lintPatternWildcard() {
        /* No restrictions */
    }
    _lintPatternVariable() {
        /* No restrictions */
    }
    _lintPatternNumber() {
        /* No restrictions */
    }
    _lintPatternStructure(pattern) {
        const name = pattern.constructorName.value;
        /* Check that the constructor exists */
        if (!this._symtable.isConstructor(name)) {
            this._failExpectedConstructorButGot(
            // throws
            pattern.startPos, pattern.endPos, name);
            return;
        }
        /* Check that the number of parameters match.
         * Note: constructor patterns with 0 arguments are always allowed.
         */
        const expected = this._symtable.constructorFields(name).length;
        const received = pattern.boundVariables.length;
        if (received > 0 && expected !== received) {
            this._lintCheck(pattern.startPos, pattern.endPos, 'structure-pattern-arity-mismatch', [
                name,
                expected,
                received
            ]);
        }
    }
    _lintPatternTuple() {
        /* No restrictions */
    }
    _lintPatternTimeout() {
        /* No restrictions */
    }
    /** Expressions **/
    // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
    _lintExpression(expression) {
        switch (expression.tag) {
            case N_ExprVariable:
                return this._lintExprVariable();
            case N_ExprConstantNumber:
                return this._lintExprConstantNumber();
            case N_ExprConstantString:
                return this._lintExprConstantString();
            case N_ExprChoose:
                return this._lintExprChoose(expression);
            case N_ExprMatching:
                return this._lintExprMatching(expression);
            case N_ExprList:
                return this._lintExprList(expression);
            case N_ExprRange:
                return this._lintExprRange(expression);
            case N_ExprTuple:
                return this._lintExprTuple(expression);
            case N_ExprStructure:
                return this._lintExprStructure(expression);
            case N_ExprStructureUpdate:
                return this._lintExprStructureUpdate(expression);
            case N_ExprFunctionCall:
                return this._lintExprFunctionCall(expression);
            default:
                throw Error('Linter: Expression not implemented: ' + Symbol.keyFor(expression.tag));
        }
    }
    _lintExprVariable() {
        /* No restrictions.
         * Note: the restriction that a variable is defined before it is used
         * is a dynamic constraint . */
    }
    _lintExprConstantNumber() {
        /* No restrictions */
    }
    _lintExprConstantString() {
        /* No restrictions */
    }
    _lintExprChoose(expression) {
        this._lintExpression(expression.condition);
        this._lintExpression(expression.trueExpr);
        this._lintExpression(expression.falseExpr);
    }
    _lintExprMatching(expression) {
        this._lintExpression(expression.subject);
        this._lintMatchingBranches(expression.branches);
    }
    _lintMatchingBranches(branches) {
        this._lintBranches(branches, false /* !isInteractiveProgram */, true /* isMatching */);
    }
    _lintExprList(expression) {
        for (const element of expression.elements) {
            this._lintExpression(element);
        }
    }
    _lintExprRange(expression) {
        this._lintExpression(expression.first);
        if (expression.second !== undefined) {
            this._lintExpression(expression.second);
        }
        this._lintExpression(expression.last);
    }
    _lintExprTuple(expression) {
        for (const element of expression.elements) {
            this._lintExpression(element);
        }
    }
    _lintExprStructure(expression) {
        this._lintExprStructureOrUpdate(expression, undefined);
    }
    _lintExprStructureUpdate(expression) {
        this._lintExprStructureOrUpdate(expression, expression.original);
    }
    /* Check a structure construction: C(x1 <- e1, ..., xN <- eN)
     * or a structure update: C(original | x1 <- e1, ..., xN <- eN).
     *
     * If original is undefined, it is a structure construction.
     * If original is not undefined, it is the updated expression.
     * */
    // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
    _lintExprStructureOrUpdate(expression, original) {
        /* Check that constructor exists */
        const constructorName = expression.constructorName.value;
        if (!this._symtable.isConstructor(constructorName)) {
            this._failExpectedConstructorButGot(
            // throws
            expression.startPos, expression.endPos, constructorName);
            return;
        }
        this._checkStructureTypeNotEvent(constructorName, expression);
        this._checkStructureNoRepeatedFields(constructorName, expression);
        this._checkStructureBindingsCorrect(constructorName, expression);
        /* If it is a structure construction, check that the fields are complete */
        if (original === undefined) {
            this._checkStructureBindingsComplete(constructorName, expression);
        }
        /* If it is an update, recursively check the original expression */
        if (original !== undefined) {
            this._lintExpression(original);
        }
        /* Recursively check expressions in field bindings */
        for (const fieldBinding of expression.fieldBindings) {
            this._lintExpression(fieldBinding.value);
        }
    }
    /* Check that there are no repeated fields in a structure
     * construction/update */
    _checkStructureNoRepeatedFields(constructorName, expression) {
        const declaredFields = expression.fieldNames();
        const seen = {};
        for (const fieldName of declaredFields) {
            if (fieldName in seen) {
                this._lintCheck(expression.startPos, expression.endPos, 'structure-construction-repeated-field', [constructorName, fieldName]);
            }
            seen[fieldName] = true;
        }
    }
    /* Check that all bindings in a structure construction/update
     * correspond to existing fields */
    _checkStructureBindingsCorrect(constructorName, expression) {
        const declaredFields = expression.fieldNames();
        const constructorFields = this._symtable.constructorFields(constructorName);
        for (const fieldName of declaredFields) {
            if (constructorFields.indexOf(fieldName) === -1) {
                this._lintCheck(expression.startPos, expression.endPos, 'structure-construction-invalid-field', [constructorName, fieldName]);
            }
        }
    }
    /* Check that bindings in a structure construction/update
     * cover all existing fields */
    _checkStructureBindingsComplete(constructorName, expression) {
        const declaredFields = expression.fieldNames();
        const constructorFields = this._symtable.constructorFields(constructorName);
        for (const fieldName of constructorFields) {
            if (declaredFields.indexOf(fieldName) === -1) {
                this._lintCheck(expression.startPos, expression.endPos, 'structure-construction-missing-field', [constructorName, fieldName]);
            }
        }
    }
    /* Check that a structure construction/update does not involve
     * constructors of the Event type, which should only be
     * handled implicitly in an interactive program. */
    _checkStructureTypeNotEvent(constructorName, expression) {
        const constructorType = this._symtable.constructorType(constructorName);
        if (constructorType === i18n$1('TYPE:Event')) {
            this._lintCheck(expression.startPos, expression.endPos, 'structure-construction-cannot-be-an-event', [constructorName]);
        }
    }
    _lintExprFunctionCall(expression) {
        /* Check that it is a function or a field */
        const name = expression.functionName.value;
        if (!this._symtable.isFunction(name) && !this._symtable.isField(name)) {
            this._lintCheck(expression.startPos, expression.endPos, 'undefined-function', [name]);
        }
        /* Check that the number of argument coincides */
        let expected;
        if (this._symtable.isFunction(name)) {
            expected = this._symtable.functionParameters(name).length;
        }
        else {
            /* Fields always have exactly one parameter */
            expected = 1;
        }
        const received = expression.args.length;
        if (expected !== received) {
            this._lintCheck(expression.startPos, expression.endPos, 'function-arity-mismatch', [
                name,
                expected,
                received
            ]);
        }
        /* Recursively check arguments */
        for (const argument of expression.args) {
            this._lintExpression(argument);
        }
    }
    _disableRecursion(ast) {
        if (this._enabledLinterChecks['forbidden-extension-allow-recursion']) {
            const cycle = new RecursionChecker().callCycle(ast);
            if (cycle !== undefined) {
                this._lintCheck(cycle[0].location.startPos, cycle[0].location.endPos, 'forbidden-extension-allow-recursion', [cycle]);
            }
        }
    }
    /* Throw a syntax error indicating that we expected the name of a
     * constructor, but we got a name which is not a constructor.
     *
     * If the name is a type or a procedure, provide a more helpful
     * error message. (Coinciding constructor and procedure names are
     * not forbidden, but it is probably a mistake). */
    _failExpectedConstructorButGot(startPos, endPos, name) {
        if (this._symtable.isType(name)) {
            this._lintCheck(startPos, endPos, 'type-used-as-constructor', [
                name,
                this._symtable.typeConstructors(name)
            ]);
        }
        else if (this._symtable.isProcedure(name)) {
            this._lintCheck(startPos, endPos, 'procedure-used-as-constructor', [name]);
        }
        else {
            this._lintCheck(startPos, endPos, 'undeclared-constructor', [name]);
        }
    }
}

/* eslint-disable no-underscore-dangle */
const isWhitespace = (chr) => chr === ' ' || chr === '\t' || chr === '\r' || chr === '\n';
const isDigit = (chr) => chr >= '0' && chr <= '9';
/* We define a character to be alphabetic if it has two distinct forms:
 * an uppercase form and a lowercase form.
 *
 * This accepts alphabetic Unicode characters but rejects numbers and symbols.
 */
const isAlpha = (chr) => chr.toUpperCase() !== chr.toLowerCase();
/* An uppercase character is an alphabetic character that coincides with
 * its uppercase form */
const isUpper = (chr) => isAlpha(chr) && chr.toUpperCase() === chr;
/* A lowercase character is an alphabetic character that coincides with
 * its lowercase form */
const isLower = (chr) => isAlpha(chr) && chr.toLowerCase() === chr;
const isIdent = (chr) => isAlpha(chr) || isDigit(chr) || chr === '_' || chr === "'";
const KEYWORDS = {
    program: T_PROGRAM,
    interactive: T_INTERACTIVE,
    procedure: T_PROCEDURE,
    function: T_FUNCTION,
    return: T_RETURN,
    /* Control structures */
    if: T_IF,
    then: T_THEN,
    elseif: T_ELSEIF,
    else: T_ELSE,
    choose: T_CHOOSE,
    when: T_WHEN,
    otherwise: T_OTHERWISE,
    repeat: T_REPEAT,
    foreach: T_FOREACH,
    in: T_IN,
    while: T_WHILE,
    switch: T_SWITCH,
    to: T_TO,
    matching: T_MATCHING,
    select: T_SELECT,
    on: T_ON,
    /* Assignment */
    let: T_LET,
    /* Operators */
    not: T_NOT,
    div: T_DIV,
    mod: T_MOD,
    /* Records/variants */
    type: T_TYPE,
    is: T_IS,
    record: T_RECORD,
    variant: T_VARIANT,
    case: T_CASE,
    field: T_FIELD,
    /* Default case in a switch/match */
    _: T_UNDERSCORE
};
/* Pattern for timeouts in an interactive program */
// eslint-disable-next-line @typescript-eslint/ban-types
const i = i18n$1('CONS:TIMEOUT');
const t = typeof i === 'string' ? i : '';
KEYWORDS[t] = T_TIMEOUT;
/* Note: the order is relevant so that the 'maximal munch' rule applies. */
const SYMBOLS = [
    /* Various delimiters */
    { symbol: '(', tag: T_LPAREN },
    { symbol: ')', tag: T_RPAREN },
    { symbol: '{', tag: T_LBRACE },
    { symbol: '}', tag: T_RBRACE },
    { symbol: '[', tag: T_LBRACK },
    { symbol: ']', tag: T_RBRACK },
    { symbol: ',', tag: T_COMMA },
    { symbol: ';', tag: T_SEMICOLON },
    { symbol: '...', tag: T_ELLIPSIS },
    /* Range operator */
    { symbol: '..', tag: T_RANGE },
    /* Assignment */
    { symbol: ':=', tag: T_ASSIGN },
    /* Logical operators */
    { symbol: '&&', tag: T_AND },
    { symbol: '||', tag: T_OR },
    /* Fields */
    { symbol: '<-', tag: T_GETS },
    { symbol: '|', tag: T_PIPE },
    /* Pattern matching */
    { symbol: '->', tag: T_ARROW },
    /* Relational operators */
    { symbol: '==', tag: T_EQ },
    { symbol: '/=', tag: T_NE },
    { symbol: '<=', tag: T_LE },
    { symbol: '>=', tag: T_GE },
    { symbol: '<', tag: T_LT },
    { symbol: '>', tag: T_GT },
    /* Functions */
    { symbol: '++', tag: T_CONCAT },
    { symbol: '+', tag: T_PLUS },
    { symbol: '-', tag: T_MINUS },
    { symbol: '*', tag: T_TIMES },
    { symbol: '^', tag: T_POW }
];
/* Valid language options accepted by the LANGUAGE pragma */
const LANGUAGE_OPTIONS = ['DestructuringForeach', 'AllowRecursion'];
const leadingZeroes = (string) => string.length >= 0 && string[0] === '0';
// eslint-disable-next-line @typescript-eslint/explicit-function-return-type
function fail$1$1(startPos, endPos, reason, args) {
    throw new GbsSyntaxError(startPos, endPos, reason, args);
}
const CLOSING_DELIMITERS = {
    '(': ')',
    '[': ']',
    '{': '}'
};
/* An instance of Lexer scans source code for tokens.
 * Example:
 *
 *     let tok = new Lexer('if (a)');
 *     tok.nextToken(); // ~~> new Token(T_IF, null, ...)
 *     tok.nextToken(); // ~~> new Token(T_LPAREN, null, ...)
 *     tok.nextToken(); // ~~> new Token(T_LOWERID, 'a', ...)
 *     tok.nextToken(); // ~~> new Token(T_RPAREN, null, ...)
 *     tok.nextToken(); // ~~> new Token(T_EOF, null, ...)
 *
 * The 'input' parameter is either a string or a mapping
 * from filenames to strings.
 */
class Lexer {
    constructor(input) {
        this._multifileReader = new MultifileReader(input);
        this._reader = this._multifileReader.readCurrentFile();
        this._warnings = [];
        /* A stack of tokens '(', '[' and '{', to provide more helpful
         * error reporting if delimiters are not balanced. */
        this._delimiterStack = [];
        /* A dictionary of pending attributes, set by the ATTRIBUTE pragma.
         * Pending attributes are used by the parser to decorate any procedure
         * or function definition. */
        this._pendingAttributes = {};
        /* A list of language options, enabled by the LANGUAGE pragma.
         * Language options are interpreted by the runner to initialize.
         * the remaining modules (linter, compiler, runtime, ...)
         * accordingly. */
        this._languageOptions = [];
    }
    /* Return the next token from the input */
    nextToken() {
        if (!this._findNextToken()) {
            const token = new Token(T_EOF, undefined, this._reader, this._reader);
            this._checkBalancedDelimiters(token);
            return token;
        }
        if (isDigit(this._reader.peek())) {
            const startPos = this._reader;
            const value = this._readStringWhile(isDigit);
            const endPos = this._reader;
            if (leadingZeroes(value) && value.length > 1) {
                fail$1$1(startPos, endPos, 'numeric-constant-should-not-have-leading-zeroes', []);
            }
            return new Token(T_NUM, value, startPos, endPos);
        }
        else if (isIdent(this._reader.peek())) {
            const startPos = this._reader;
            const value = this._readStringWhile(isIdent);
            const endPos = this._reader;
            if (value in KEYWORDS) {
                return new Token(KEYWORDS[value], value, startPos, endPos);
            }
            else if (isUpper(value[0])) {
                return new Token(T_UPPERID, value, startPos, endPos);
            }
            else if (isLower(value[0])) {
                return new Token(T_LOWERID, value, startPos, endPos);
            }
            else {
                fail$1$1(startPos, endPos, 'identifier-must-start-with-alphabetic-character', []);
            }
        }
        else if (this._reader.peek() === '"') {
            return this._readStringConstant();
        }
        else {
            return this._readSymbol();
        }
    }
    /* When tokenization is done, this function returns the list of all
     * the warnings collected during tokenization */
    warnings() {
        return this._warnings;
    }
    /* Skip whitespace and advance through files until the start of the next
     * token is found. Return false if EOF is found. */
    _findNextToken() {
        for (;;) {
            this._ignoreWhitespaceAndComments();
            if (!this._reader.eof()) {
                break;
            }
            if (this._multifileReader.moreFiles()) {
                this._multifileReader.nextFile();
                this._reader = this._multifileReader.readCurrentFile();
            }
            else {
                return false;
            }
        }
        return true;
    }
    /* Read a string while the given condition holds for the current
     * character */
    // eslint-disable-next-line @typescript-eslint/ban-types
    _readStringWhile(condition) {
        const result = [];
        while (!this._reader.eof()) {
            if (!condition(this._reader.peek())) {
                break;
            }
            result.push(this._reader.peek());
            this._reader = this._reader.consumeCharacter();
        }
        return result.join('');
    }
    /* Reads a quote-delimited string constant.
     * Escapes are recognized. */
    _readStringConstant() {
        const startPos = this._reader;
        const result = [];
        this._reader = this._reader.consumeCharacter();
        while (!this._reader.eof()) {
            const c = this._reader.peek();
            if (c === '"') {
                this._reader = this._reader.consumeCharacter();
                return new Token(T_STRING, result.join(''), startPos, this._reader);
            }
            else if (c === '\\') {
                this._reader = this._reader.consumeCharacter();
                if (this._reader.eof()) {
                    break;
                }
                const c2 = this._reader.peek();
                this._reader = this._reader.consumeCharacter();
                switch (c2) {
                    case 'a':
                        result.push('\u0007');
                        break;
                    case 'b':
                        result.push('\u0008');
                        break;
                    case 'f':
                        result.push('\u000c');
                        break;
                    case 'n':
                        result.push('\u000a');
                        break;
                    case 'r':
                        result.push('\u000d');
                        break;
                    case 't':
                        result.push('\u0009');
                        break;
                    case 'v':
                        result.push('\u000b');
                        break;
                    default:
                        result.push(c2);
                        break;
                }
            }
            else {
                result.push(c);
                this._reader = this._reader.consumeCharacter();
            }
        }
        fail$1$1(startPos, this._reader, 'unclosed-string-constant', []);
    }
    /* Read a symbol */
    _readSymbol() {
        for (const { symbol, tag } of SYMBOLS) {
            if (this._reader.startsWith(symbol)) {
                const startPos = this._reader;
                this._reader = this._reader.consumeString(symbol);
                const endPos = this._reader;
                const token = new Token(tag, symbol, startPos, endPos);
                this._checkBalancedDelimiters(token);
                return token;
            }
        }
        fail$1$1(this._reader, this._reader, 'unknown-token', [this._reader.peek()]);
    }
    _ignoreWhitespaceAndComments() {
        while (this._ignoreWhitespace() || this._ignoreComments()) {
            /* continue */
        }
    }
    _ignoreWhitespace() {
        if (!this._reader.eof() && isWhitespace(this._reader.peek())) {
            this._reader = this._reader.consumeCharacter();
            return true;
        }
        else {
            return false;
        }
    }
    /* Skips comments and pragmas, returns false if there are no comments */
    _ignoreComments() {
        if (this._startSingleLineComment()) {
            this._ignoreSingleLineComment();
            return true;
        }
        else if (this._reader.startsWith('/*@')) {
            const startPos = this._reader;
            this._evaluatePragma(startPos, this._readInvisiblePragma('/*', '*/', '@'));
            return true;
        }
        else if (this._reader.startsWith('{-')) {
            this._ignoreMultilineComment('{-', '-}');
            return true;
        }
        else if (this._reader.startsWith('/*')) {
            this._ignoreMultilineComment('/*', '*/');
            return true;
        }
        else {
            return false;
        }
    }
    /* Returns true if a single-line comment starts here */
    _startSingleLineComment() {
        return (this._reader.startsWith('--') ||
            this._reader.startsWith('//') ||
            this._reader.startsWith('#'));
    }
    /* Skips a single-line comment */
    _ignoreSingleLineComment() {
        while (!this._reader.eof()) {
            this._reader = this._reader.consumeCharacter();
            if (this._reader.peek() === '\n') {
                break;
            }
        }
    }
    /* Skips a multiline comment with the given left/right delimiters.
     * Multi-line comments may be nested. */
    _ignoreMultilineComment(left, right) {
        let nesting = 0;
        const startPos = this._reader;
        while (!this._reader.eof()) {
            if (this._reader.startsWith(left)) {
                this._reader = this._reader.consumeString(left);
                nesting++;
            }
            else if (this._reader.startsWith(right)) {
                this._reader = this._reader.consumeString(right);
                nesting--;
                if (nesting === 0) {
                    return;
                }
            }
            else {
                this._reader = this._reader.consumeCharacter();
            }
        }
        fail$1$1(startPos, this._reader, 'unclosed-multiline-comment', []);
    }
    /* Read a pragma. A pragma is a comment delimited by the
     * given left   / *
     * and right    * /
     * comment delimiters.
     * It has N >= 0 parts delimited by the pragma delimiter   @
     *   @part1@part2@...@partN@
     */
    _readInvisiblePragma(left, right, pragmaDelim) {
        const pragma = [];
        const startPos = this._reader;
        this._reader = this._reader.consumeInvisibleString(left);
        this._reader = this._reader.consumeInvisibleString(pragmaDelim);
        while (!this._reader.eof()) {
            pragma.push(this._readInvisibleStringUntilDelimiter(pragmaDelim));
            this._reader = this._reader.consumeInvisibleString(pragmaDelim);
            if (this._reader.startsWith(right)) {
                this._reader = this._reader.consumeInvisibleString(right);
                return pragma;
            }
        }
        fail$1$1(startPos, this._reader, 'unclosed-multiline-comment', []);
    }
    /* Read an invisible string until the given delimiter is found */
    _readInvisibleStringUntilDelimiter(delimiter) {
        const startPos = this._reader;
        const result = [];
        while (!this._reader.eof()) {
            if (this._reader.peek() === delimiter) {
                return result.join('');
            }
            result.push(this._reader.peek());
            this._reader = this._reader.consumeInvisibleCharacter();
        }
        fail$1$1(startPos, this._reader, 'unclosed-multiline-comment', []);
    }
    _evaluatePragma(startPos, pragma) {
        if (pragma.length === 0) {
            this._emitWarning(startPos, this._reader, 'empty-pragma', []);
        }
        else if (pragma[0] === 'BEGIN_REGION') {
            const region = pragma[1];
            this._reader = this._reader.beginRegion(region);
        }
        else if (pragma[0] === 'END_REGION') {
            this._reader = this._reader.endRegion();
        }
        else if (pragma[0] === 'ATTRIBUTE' && pragma.length >= 2) {
            const key = pragma[1];
            const value = pragma.slice(2, pragma.length).join('@');
            this.setAttribute(key, value);
        }
        else if (pragma[0] === 'LANGUAGE' && pragma.length === 2) {
            const languageOption = pragma[1];
            this.addLanguageOption(languageOption);
        }
        else {
            this._emitWarning(startPos, this._reader, 'unknown-pragma', [pragma[0]]);
        }
    }
    _emitWarning(startPos, endPos, reason, args) {
        this._warnings.push(new GbsWarning(startPos, endPos, reason, args));
    }
    /* Check that reading a delimiter keeps the delimiter stack balanced. */
    _checkBalancedDelimiters(token) {
        if (token.tag === T_EOF && this._delimiterStack.length > 0) {
            const openingDelimiter = this._delimiterStack.pop();
            fail$1$1(openingDelimiter.startPos, openingDelimiter.endPos, 'unmatched-opening-delimiter', [openingDelimiter.value]);
        }
        else if (token.tag === T_LPAREN || token.tag === T_LBRACE || token.tag === T_LBRACK) {
            this._delimiterStack.push(token);
        }
        else if (token.tag === T_RPAREN || token.tag === T_RBRACE || token.tag === T_RBRACK) {
            if (this._delimiterStack.length === 0) {
                fail$1$1(token.startPos, token.endPos, 'unmatched-closing-delimiter', [token.value]);
            }
            const openingDelimiter = this._delimiterStack.pop();
            if (CLOSING_DELIMITERS[openingDelimiter.value] !== token.value) {
                fail$1$1(openingDelimiter.startPos, openingDelimiter.endPos, 'unmatched-opening-delimiter', [openingDelimiter.value]);
            }
        }
    }
    /*
     * Interface for handling attributes.
     *
     * The pragma ATTRIBUTE@key@value
     * establishes the attribute given by <key> to <value>.
     *
     * Whenever the parser finds a definition of the following kinds:
     *   procedure
     *   function
     *   program
     *   interactive program
     *   type
     * it gets decorated with the pending attributes.
     */
    getPendingAttributes() {
        const a = this._pendingAttributes;
        this._pendingAttributes = {};
        return a;
    }
    // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
    setAttribute(key, value) {
        this._pendingAttributes[key] = value;
    }
    /*
     * Interface for handling language options.
     *
     * The pragma LANGUAGE@option sets the given option.
     *
     * The runner module reads these options to initialize the
     * linter/compiler/runtime.
     */
    getLanguageOptions() {
        return this._languageOptions;
    }
    addLanguageOption(option) {
        if (LANGUAGE_OPTIONS.indexOf(option) !== -1) {
            this._languageOptions.push(option);
        }
        else {
            fail$1$1(this._reader, this._reader, 'unknown-language-option', [option]);
        }
    }
}

/* eslint-disable camelcase */
// Only for typing purposes
// eslint-disable-next-line @typescript-eslint/ban-types
const toFunc$3 = (x) => x;
// Only for typing purposes
// eslint-disable-next-line @typescript-eslint/ban-types
const toStr = (x) => x;
const Infix = Symbol.for('Infix');
const InfixL = Symbol.for('InfixL');
const InfixR = Symbol.for('InfixR');
const Prefix = Symbol.for('Prefix');
class PrecedenceLevel {
    /* Operators should be a dictionary mapping operator tags to
     * their function names */
    constructor(fixity, operators) {
        this._fixity = fixity;
        this._operators = operators;
    }
    get fixity() {
        return this._fixity;
    }
    isOperator(token) {
        return Symbol.keyFor(token.tag) in this._operators;
    }
    functionName(token) {
        return new Token(T_LOWERID, this._operators[Symbol.keyFor(token.tag)], token.startPos, token.endPos);
    }
}
/* OPERATORS is a list of precedence levels.
 * Precedence levels are ordered from lesser to greater precedence.
 */
const OPERATORS = [
    /* Logical operators */
    new PrecedenceLevel(InfixR, {
        T_OR: '||'
    }),
    new PrecedenceLevel(InfixR, {
        T_AND: '&&'
    }),
    new PrecedenceLevel(Prefix, {
        T_NOT: 'not'
    }),
    /* Relational operators */
    new PrecedenceLevel(Infix, {
        T_EQ: '==',
        T_NE: '/=',
        T_LE: '<=',
        T_GE: '>=',
        T_LT: '<',
        T_GT: '>'
    }),
    /* List concatenation */
    new PrecedenceLevel(InfixL, {
        T_CONCAT: '++'
    }),
    /* Additive operators */
    new PrecedenceLevel(InfixL, {
        T_PLUS: '+',
        T_MINUS: '-'
    }),
    /* Multiplicative operators */
    new PrecedenceLevel(InfixL, {
        T_TIMES: '*'
    }),
    /* Division operators */
    new PrecedenceLevel(InfixL, {
        T_DIV: 'div',
        T_MOD: 'mod'
    }),
    /* Exponential operators */
    new PrecedenceLevel(InfixR, {
        T_POW: '^'
    }),
    /* Unary minus */
    new PrecedenceLevel(Prefix, {
        T_MINUS: '-(unary)'
    })
];
function fail$4(startPos, endPos, reason, args) {
    throw new GbsSyntaxError(startPos, endPos, reason, args);
}
/* Represents a parser for a Gobstones/XGobstones program.
 * It is structured as a straightforward recursive-descent parser.
 *
 * The parameter 'input' may be either a string or a dictionary
 * mapping filenames to strings.
 *
 * All the "parseFoo" methods agree to the following convention:
 * - parseFoo returns an AST for a Foo construction,
 * - parseFoo consumes a fragment of the input by successively requesting
 *   the next token from the lexer,
 * - when calling parseFoo, the current token should already be located
 *   on the first token of the corresponding construction,
 * - when parseFoo returns, the current token is already located on
 *   the following token, after the corresponding construction.
 */
class Parser {
    constructor(input) {
        this._lexer = new Lexer(input);
        this._nextToken();
    }
    /* Return the AST that results from parsing a full program */
    parse() {
        const definitions = [];
        while (this._currentToken.tag !== T_EOF) {
            definitions.push(this._parseDefinition());
        }
        return new ASTMain(definitions);
    }
    /* Return the list of all language options collected by the tokenizer.
     * Language options are set by the LANGUAGE pragma. */
    getLanguageOptions() {
        return this._lexer.getLanguageOptions();
    }
    /** Definitions **/
    _parseDefinition() {
        switch (this._currentToken.tag) {
            case T_PROGRAM:
                return this._parseDefProgram();
            case T_INTERACTIVE:
                return this._parseDefInteractiveProgram();
            case T_PROCEDURE:
                return this._parseDefProcedure();
            case T_FUNCTION:
                return this._parseDefFunction();
            case T_TYPE:
                return this._parseDefType();
            default:
                fail$4(this._currentToken.startPos, this._currentToken.endPos, 'expected-but-found', [
                    i18n$1('definition'),
                    i18n$1(Symbol.keyFor(this._currentToken.tag))
                ]);
        }
    }
    _parseDefProgram() {
        const startPos = this._currentToken.startPos;
        this._match(T_PROGRAM);
        const attributes = this._lexer.getPendingAttributes();
        const block = this._parseStmtBlock();
        const result = new ASTDefProgram(block);
        result.startPos = startPos;
        result.endPos = block.endPos;
        result.attributes = attributes;
        return result;
    }
    _parseDefInteractiveProgram() {
        const startPos = this._currentToken.startPos;
        this._match(T_INTERACTIVE);
        this._match(T_PROGRAM);
        const attributes = this._lexer.getPendingAttributes();
        this._match(T_LBRACE);
        const branches = this._parseSwitchBranches();
        const endPos = this._currentToken.startPos;
        this._match(T_RBRACE);
        const result = new ASTDefInteractiveProgram(branches);
        result.startPos = startPos;
        result.endPos = endPos;
        result.attributes = attributes;
        return result;
    }
    _parseDefProcedure() {
        const startPos = this._currentToken.startPos;
        this._match(T_PROCEDURE);
        const name = this._parseUpperid();
        this._match(T_LPAREN);
        const parameters = this._parseLoweridSeq();
        this._match(T_RPAREN);
        const attributes = this._lexer.getPendingAttributes();
        const block = this._parseStmtBlock();
        const result = new ASTDefProcedure(name, parameters, block);
        result.startPos = startPos;
        result.endPos = block.endPos;
        result.attributes = attributes;
        return result;
    }
    _parseDefFunction() {
        const startPos = this._currentToken.startPos;
        this._match(T_FUNCTION);
        const name = this._currentToken;
        this._match(T_LOWERID);
        this._match(T_LPAREN);
        const parameters = this._parseLoweridSeq();
        this._match(T_RPAREN);
        const attributes = this._lexer.getPendingAttributes();
        const block = this._parseStmtBlock();
        const result = new ASTDefFunction(name, parameters, block);
        result.startPos = startPos;
        result.endPos = block.endPos;
        result.attributes = attributes;
        return result;
    }
    _parseDefType() {
        const startPos = this._currentToken.startPos;
        this._match(T_TYPE);
        const typeName = this._parseUpperid();
        this._match(T_IS);
        switch (this._currentToken.tag) {
            case T_RECORD:
                return this._parseDefTypeRecord(startPos, typeName);
            case T_VARIANT:
                return this._parseDefTypeVariant(startPos, typeName);
            default:
                fail$4(this._currentToken.startPos, this._currentToken.endPos, 'expected-but-found', [
                    toFunc$3(i18n$1('<alternative>'))([i18n$1('T_RECORD'), i18n$1('T_VARIANT')]),
                    i18n$1(Symbol.keyFor(this._currentToken.tag))
                ]);
        }
    }
    _parseDefTypeRecord(startPos, typeName) {
        this._match(T_RECORD);
        const attributes = this._lexer.getPendingAttributes();
        this._match(T_LBRACE);
        const fieldNames = this._parseFieldNames();
        const endPos = this._currentToken.startPos;
        this._matchExpected(T_RBRACE, [T_FIELD, T_RBRACE]);
        const result = new ASTDefType(typeName, [
            new ASTConstructorDeclaration(typeName, fieldNames)
        ]);
        result.startPos = startPos;
        result.endPos = endPos;
        result.attributes = attributes;
        return result;
    }
    _parseDefTypeVariant(startPos, typeName) {
        const constructorDeclarations = [];
        this._match(T_VARIANT);
        const attributes = this._lexer.getPendingAttributes();
        this._match(T_LBRACE);
        while (this._currentToken.tag === T_CASE) {
            constructorDeclarations.push(this._parseConstructorDeclaration());
        }
        const endPos = this._currentToken.startPos;
        this._matchExpected(T_RBRACE, [T_CASE, T_RBRACE]);
        const result = new ASTDefType(typeName, constructorDeclarations);
        result.startPos = startPos;
        result.endPos = endPos;
        result.attributes = attributes;
        return result;
    }
    _parseConstructorDeclaration() {
        const startPos = this._currentToken.startPos;
        this._match(T_CASE);
        const constructorName = this._parseUpperid();
        this._match(T_LBRACE);
        const fieldNames = this._parseFieldNames();
        const endPos = this._currentToken.startPos;
        this._matchExpected(T_RBRACE, [T_FIELD, T_RBRACE]);
        const result = new ASTConstructorDeclaration(constructorName, fieldNames);
        result.startPos = startPos;
        result.endPos = endPos;
        return result;
    }
    _parseFieldNames() {
        const fieldNames = [];
        while (this._currentToken.tag === T_FIELD) {
            this._match(T_FIELD);
            fieldNames.push(this._parseLowerid());
        }
        return fieldNames;
    }
    /** Statements **/
    /* Statement, optionally followed by semicolon */
    _parseStatement() {
        const statement = this._parsePureStatement();
        if (this._currentToken.tag === T_SEMICOLON) {
            this._match(T_SEMICOLON);
        }
        return statement;
    }
    /* Statement (not followed by semicolon) */
    _parsePureStatement() {
        switch (this._currentToken.tag) {
            case T_ELLIPSIS:
                return this._parseStmtEllipsis();
            case T_RETURN:
                return this._parseStmtReturn();
            case T_IF:
                return this._parseStmtIf(true /* expectInitialIf */);
            case T_REPEAT:
                return this._parseStmtRepeat();
            case T_FOREACH:
                return this._parseStmtForeach();
            case T_WHILE:
                return this._parseStmtWhile();
            case T_SWITCH:
                return this._parseStmtSwitch();
            case T_LET:
                return this._parseStmtLet();
            case T_LBRACE:
                return this._parseStmtBlock();
            case T_LOWERID:
                return this._parseStmtAssignVariable();
            case T_UPPERID:
                return this._parseStmtProcedureCall();
            case T_LPAREN:
                /* Special error for rejecting tuple assignments
                 *   (x1, ..., xN) := expression
                 * in favour of
                 *   let (x1, ..., xN) := expression
                 */
                fail$4(this._currentToken.startPos, this._currentToken.endPos, 'obsolete-tuple-assignment', []);
                return;
            default:
                fail$4(this._currentToken.startPos, this._currentToken.endPos, 'expected-but-found', [
                    i18n$1('statement'),
                    i18n$1(Symbol.keyFor(this._currentToken.tag))
                ]);
        }
    }
    _parseStmtBlock() {
        const startPos = this._currentToken.startPos;
        const statements = [];
        this._match(T_LBRACE);
        while (this._currentToken.tag !== T_RBRACE) {
            statements.push(this._parseStatement());
            if (this._currentToken.tag === T_SEMICOLON) {
                this._match(T_SEMICOLON);
            }
        }
        const endPos = this._currentToken.startPos;
        this._match(T_RBRACE);
        const result = new ASTStmtBlock(statements);
        result.startPos = startPos;
        result.endPos = endPos;
        return result;
    }
    _parseStmtEllipsis() {
        const startPos = this._currentToken.startPos;
        this._match(T_ELLIPSIS);
        const result = new ASTStmtProcedureCall(new Token(T_UPPERID, toStr(i18n$1('PRIM:BOOM')), startPos, startPos), [new ASTExprConstantString(new Token(T_STRING, toStr(i18n$1('errmsg:ellipsis'))))]);
        result.startPos = startPos;
        result.endPos = this._currentToken.startPos;
        return result;
    }
    _parseStmtReturn() {
        const startPos = this._currentToken.startPos;
        this._match(T_RETURN);
        const tuple = this._parseExprTuple(false /* possiblyEmpty */);
        const result = new ASTStmtReturn(tuple);
        result.startPos = startPos;
        result.endPos = tuple.endPos;
        return result;
    }
    _parseStmtIf(expectInitialIf) {
        const startPos = this._currentToken.startPos;
        if (expectInitialIf) {
            this._match(T_IF);
        }
        this._match(T_LPAREN);
        const condition = this._parseExpression();
        this._match(T_RPAREN);
        /* Optional 'then' */
        if (this._currentToken.tag === T_THEN) {
            this._match(T_THEN);
        }
        const thenBlock = this._parseStmtBlock();
        let endPos;
        let elseBlock;
        if (this._currentToken.tag === T_ELSEIF) {
            this._match(T_ELSEIF);
            elseBlock = this._parseStmtIf(false /* expectInitialIf */);
            endPos = elseBlock.endPos;
        }
        else if (this._currentToken.tag === T_ELSE) {
            this._match(T_ELSE);
            elseBlock = this._parseStmtBlock();
            endPos = elseBlock.endPos;
        }
        else {
            elseBlock = undefined;
            endPos = thenBlock.endPos;
        }
        const result = new ASTStmtIf(condition, thenBlock, elseBlock);
        result.startPos = startPos;
        result.endPos = endPos;
        return result;
    }
    _parseStmtRepeat() {
        const startPos = this._currentToken.startPos;
        this._match(T_REPEAT);
        this._match(T_LPAREN);
        const times = this._parseExpression();
        this._match(T_RPAREN);
        const body = this._parseStmtBlock();
        const result = new ASTStmtRepeat(times, body);
        result.startPos = startPos;
        result.endPos = body.endPos;
        return result;
    }
    _parseStmtForeach() {
        const startPos = this._currentToken.startPos;
        this._match(T_FOREACH);
        const pattern = this._parsePattern();
        this._match(T_IN);
        const range = this._parseExpression();
        const body = this._parseStmtBlock();
        const result = new ASTStmtForeach(pattern, range, body);
        result.startPos = startPos;
        result.endPos = body.endPos;
        return result;
    }
    _parseStmtWhile() {
        const startPos = this._currentToken.startPos;
        this._match(T_WHILE);
        this._match(T_LPAREN);
        const condition = this._parseExpression();
        this._match(T_RPAREN);
        const body = this._parseStmtBlock();
        const result = new ASTStmtWhile(condition, body);
        result.startPos = startPos;
        result.endPos = body.endPos;
        return result;
    }
    _parseStmtSwitch() {
        const startPos = this._currentToken.startPos;
        this._match(T_SWITCH);
        this._match(T_LPAREN);
        const subject = this._parseExpression();
        this._match(T_RPAREN);
        if (this._currentToken.tag === T_TO) {
            this._match(T_TO);
        }
        this._match(T_LBRACE);
        const branches = this._parseSwitchBranches();
        const endPos = this._currentToken.startPos;
        this._match(T_RBRACE);
        const result = new ASTStmtSwitch(subject, branches);
        result.startPos = startPos;
        result.endPos = endPos;
        return result;
    }
    _parseStmtLet() {
        const startPos = this._currentToken.startPos;
        this._match(T_LET);
        let result;
        if (this._currentToken.tag === T_LOWERID) {
            result = this._parseStmtAssignVariable();
        }
        else if (this._currentToken.tag === T_LPAREN) {
            result = this._parseStmtAssignTuple();
        }
        else {
            fail$4(this._currentToken.startPos, this._currentToken.endPos, 'expected-but-found', [
                toFunc$3(i18n$1('<alternative>'))(i18n$1('T_LOWERID'), i18n$1('T_LPAREN')),
                toStr(i18n$1(Symbol.keyFor(this._currentToken.tag)))
            ]);
        }
        result.startPos = startPos;
        return result;
    }
    _parseStmtAssignVariable() {
        const variable = this._parseLowerid();
        this._match(T_ASSIGN);
        const value = this._parseExpression();
        const result = new ASTStmtAssignVariable(variable, value);
        result.startPos = variable.startPos;
        result.endPos = value.endPos;
        return result;
    }
    _parseStmtAssignTuple() {
        const startPos = this._currentToken.startPos;
        this._match(T_LPAREN);
        const variables = this._parseLoweridSeq();
        if (variables.length === 1) {
            fail$4(startPos, this._currentToken.endPos, 'assignment-tuple-cannot-be-singleton', []);
        }
        this._match(T_RPAREN);
        this._match(T_ASSIGN);
        const value = this._parseExpression();
        const result = new ASTStmtAssignTuple(variables, value);
        result.startPos = startPos;
        result.endPos = value.endPos;
        return result;
    }
    _parseStmtProcedureCall() {
        const procedureName = this._parseUpperid();
        this._match(T_LPAREN);
        const args = this._parseDelimitedSeq(T_RPAREN, T_COMMA, () => this._parseExpression());
        const endPos = this._currentToken.startPos;
        this._match(T_RPAREN);
        const result = new ASTStmtProcedureCall(procedureName, args);
        result.startPos = procedureName.startPos;
        result.endPos = endPos;
        return result;
    }
    /** Patterns **/
    _parsePattern() {
        switch (this._currentToken.tag) {
            case T_UNDERSCORE:
                return this._parsePatternWildcard();
            case T_LOWERID:
                return this._parsePatternVariable();
            case T_NUM:
            case T_MINUS:
                return this._parsePatternNumber();
            case T_UPPERID:
                return this._parsePatternStructure();
            case T_LPAREN:
                return this._parsePatternTuple();
            case T_TIMEOUT:
                return this._parsePatternTimeout();
            default:
                fail$4(this._currentToken.startPos, this._currentToken.endPos, 'expected-but-found', [
                    i18n$1('pattern'),
                    i18n$1(Symbol.keyFor(this._currentToken.tag))
                ]);
        }
    }
    _parsePatternWildcard() {
        const startPos = this._currentToken.startPos;
        this._match(T_UNDERSCORE);
        const result = new ASTPatternWildcard();
        const endPos = startPos;
        result.startPos = startPos;
        result.endPos = endPos;
        return result;
    }
    _parsePatternVariable() {
        const startPos = this._currentToken.startPos;
        const id = this._parseLowerid();
        const result = new ASTPatternVariable(id);
        result.startPos = startPos;
        result.endPos = id.endPos;
        return result;
    }
    _parsePatternNumber() {
        const startPos = this._currentToken.startPos;
        let sign = '';
        if (this._currentToken.tag === T_MINUS) {
            this._match(T_MINUS);
            sign = '-';
        }
        let number = this._currentToken;
        this._match(T_NUM);
        const value = sign + number.value;
        if (value === '-0') {
            fail$4(startPos, number.endPos, 'pattern-number-cannot-be-negative-zero', []);
        }
        number = new Token(T_NUM, value, number.startPos, number.endPos);
        const result = new ASTPatternNumber(number);
        result.startPos = startPos;
        result.endPos = number.endPos;
        return result;
    }
    _parsePatternStructure() {
        const startPos = this._currentToken.startPos;
        let endPos = this._currentToken.startPos;
        const constructor = this._parseUpperid();
        let parameters;
        if (this._currentToken.tag === T_LPAREN) {
            this._match(T_LPAREN);
            parameters = this._parseLoweridSeq();
            endPos = this._currentToken.startPos;
            this._match(T_RPAREN);
        }
        else {
            parameters = [];
        }
        const result = new ASTPatternStructure(constructor, parameters);
        result.startPos = startPos;
        result.endPos = endPos;
        return result;
    }
    _parsePatternTuple() {
        const startPos = this._currentToken.startPos;
        this._match(T_LPAREN);
        const parameters = this._parseLoweridSeq();
        if (parameters.length === 1) {
            fail$4(startPos, this._currentToken.endPos, 'pattern-tuple-cannot-be-singleton', []);
        }
        const endPos = this._currentToken.startPos;
        this._match(T_RPAREN);
        const result = new ASTPatternTuple(parameters);
        result.startPos = startPos;
        result.endPos = endPos;
        return result;
    }
    _parsePatternTimeout() {
        const startPos = this._currentToken.startPos;
        this._match(T_TIMEOUT);
        this._match(T_LPAREN);
        const timeout = this._currentToken;
        this._match(T_NUM);
        const endPos = this._currentToken.startPos;
        this._match(T_RPAREN);
        const result = new ASTPatternTimeout(timeout);
        result.startPos = startPos;
        result.endPos = endPos;
        return result;
    }
    /** Expressions **/
    _parseExpression() {
        return this._parseExprOperator(0);
    }
    /* Read an expression of the given level.
     *
     * If the list OPERATORS of precedence levels has N elements, then:
     * - Expressions of level 0 are arbitrary expressions.
     * - Expressions of level N are atomic expressions.
     * - In general, expressions of level I involve operators
     *   of levels I, I+1, ..., N-1,
     *   and they can only include operators of the lower levels
     *   by surrounding them in parentheses.
     */
    _parseExprOperator(level) {
        if (level === OPERATORS.length) {
            return this._parseExprAtom();
        }
        switch (OPERATORS[level].fixity) {
            case Infix:
                return this._parseExprOperatorInfix(level);
            case InfixL:
                return this._parseExprOperatorInfixL(level);
            case InfixR:
                return this._parseExprOperatorInfixR(level);
            case Prefix:
                return this._parseExprOperatorPrefix(level);
            default:
                throw Error('Invalid operator.');
        }
    }
    _parseExprOperatorInfix(level) {
        const left = this._parseExprOperator(level + 1);
        if (OPERATORS[level].isOperator(this._currentToken)) {
            const op = this._currentToken;
            this._nextToken();
            const right = this._parseExprOperator(level + 1);
            /* Check that it is not used associatively */
            if (OPERATORS[level].isOperator(this._currentToken)) {
                fail$4(this._currentToken.startPos, this._currentToken.endPos, 'operators-are-not-associative', [i18n$1(Symbol.keyFor(op.tag)), i18n$1(Symbol.keyFor(this._currentToken.tag))]);
            }
            const result = new ASTExprFunctionCall(OPERATORS[level].functionName(op), [
                left,
                right
            ]);
            result.startPos = left.startPos;
            result.endPos = right.endPos;
            return result;
        }
        else {
            return left;
        }
    }
    _parseExprOperatorInfixL(level) {
        let result = this._parseExprOperator(level + 1);
        while (OPERATORS[level].isOperator(this._currentToken)) {
            const op = this._currentToken;
            this._nextToken();
            const right = this._parseExprOperator(level + 1);
            const result2 = new ASTExprFunctionCall(OPERATORS[level].functionName(op), [
                result,
                right
            ]);
            result2.startPos = result.startPos;
            result2.endPos = right.endPos;
            result = result2;
        }
        return result;
    }
    _parseExprOperatorInfixR(level) {
        const left = this._parseExprOperator(level + 1);
        if (OPERATORS[level].isOperator(this._currentToken)) {
            const op = this._currentToken;
            this._nextToken();
            const right = this._parseExprOperator(level); /* same level */
            const result = new ASTExprFunctionCall(OPERATORS[level].functionName(op), [
                left,
                right
            ]);
            result.startPos = left.startPos;
            result.endPos = right.endPos;
            return result;
        }
        else {
            return left;
        }
    }
    _parseExprOperatorPrefix(level) {
        if (OPERATORS[level].isOperator(this._currentToken)) {
            const op = this._currentToken;
            this._nextToken();
            const inner = this._parseExprOperator(level); /* same level */
            const result = new ASTExprFunctionCall(OPERATORS[level].functionName(op), [inner]);
            result.startPos = op.startPos;
            result.endPos = inner.endPos;
            return result;
        }
        else {
            return this._parseExprOperator(level + 1);
        }
    }
    /* Parse an atomic expression.
     * I.e. all the operators must be surrounded by parentheses */
    _parseExprAtom() {
        switch (this._currentToken.tag) {
            case T_ELLIPSIS:
                return this._parseExprEllipsis();
            case T_LOWERID:
                return this._parseExprVariableOrFunctionCall();
            case T_NUM:
                return this._parseExprConstantNumber();
            case T_STRING:
                return this._parseExprConstantString();
            case T_CHOOSE:
                return this._parseExprChoose(true /* expectInitialChoose */);
            case T_MATCHING:
                return this._parseExprMatching();
            case T_UPPERID:
                return this._parseExprStructureOrStructureUpdate();
            case T_LPAREN:
                return this._parseExprTuple(true /* possiblyEmpty */);
            case T_LBRACK:
                return this._parseExprListOrRange();
            default:
                fail$4(this._currentToken.startPos, this._currentToken.endPos, 'expected-but-found', [
                    i18n$1('expression'),
                    i18n$1(Symbol.keyFor(this._currentToken.tag))
                ]);
        }
    }
    _parseExprEllipsis() {
        const startPos = this._currentToken.startPos;
        this._match(T_ELLIPSIS);
        const result = new ASTExprFunctionCall(new Token(T_LOWERID, toStr(i18n$1('PRIM:boom')), startPos, startPos), [new ASTExprConstantString(new Token(T_STRING, toStr(i18n$1('errmsg:ellipsis'))))]);
        result.startPos = startPos;
        result.endPos = this._currentToken.startPos;
        return result;
    }
    _parseExprVariableOrFunctionCall() {
        const id = this._parseLowerid();
        let result;
        let endPos;
        if (this._currentToken.tag === T_LPAREN) {
            this._match(T_LPAREN);
            const args = this._parseExpressionSeq(T_RPAREN);
            result = new ASTExprFunctionCall(id, args);
            endPos = this._currentToken.startPos;
            this._match(T_RPAREN);
        }
        else {
            result = new ASTExprVariable(id);
            endPos = id.endPos;
        }
        result.startPos = id.startPos;
        result.endPos = endPos;
        return result;
    }
    _parseExprConstantNumber() {
        const number = this._currentToken;
        this._match(T_NUM);
        const result = new ASTExprConstantNumber(number);
        result.startPos = number.startPos;
        result.endPos = number.endPos;
        return result;
    }
    _parseExprConstantString() {
        const string = this._currentToken;
        this._match(T_STRING);
        const result = new ASTExprConstantString(string);
        result.startPos = string.startPos;
        result.endPos = string.endPos;
        return result;
    }
    _parseExprChoose(expectInitialChoose) {
        const startPos = this._currentToken.startPos;
        if (expectInitialChoose) {
            this._match(T_CHOOSE);
        }
        const expr1 = this._parseExpression();
        if (this._currentToken.tag === T_WHEN) {
            this._match(T_WHEN);
            this._match(T_LPAREN);
            const condition = this._parseExpression();
            this._match(T_RPAREN);
            const expr2 = this._parseExprChoose(false /* expectInitialChoose */);
            const result = new ASTExprChoose(condition, expr1, expr2);
            result.startPos = startPos;
            result.endPos = expr2.endPos;
            return result;
        }
        else {
            const endPos = this._currentToken.endPos;
            this._match(T_OTHERWISE);
            expr1.startPos = startPos;
            expr1.endPos = endPos;
            return expr1;
        }
    }
    _parseExprMatching() {
        const startPos = this._currentToken.startPos;
        this._match(T_MATCHING);
        this._match(T_LPAREN);
        const subject = this._parseExpression();
        this._match(T_RPAREN);
        this._match(T_SELECT);
        const branches = this._parseMatchingBranches();
        const result = new ASTExprMatching(subject, branches);
        result.startPos = startPos;
        // result.endPos = result.endPos;
        return result;
    }
    /*
     * Parse any of the following constructions:
     * (1) Structure with no arguments: "Norte"
     * (2) Structure with no arguments and explicit parentheses: "Nil()"
     * (3) Structure with arguments: "Coord(x <- 1, y <- 2)"
     * (4) Update structure with arguments: "Coord(expression | x <- 2)"
     *
     * Deciding between (3) and (4) unfortunately cannot be done with one
     * token of lookahead, so after reading the constructor and a left
     * parenthesis we resort to the following workaround:
     *
     * - Parse an expression.
     * - If the next token is GETS ("<-") we are in case (3).
     *   We must then ensure that the expression is just a variable
     *   and recover its name.
     * - If the next token is PIPE ("|") we are in case (4), and we go on.
     */
    _parseExprStructureOrStructureUpdate() {
        const constructorName = this._parseUpperid();
        if (this._currentToken.tag !== T_LPAREN) {
            /* Structure with no arguments, e.g. "Norte" */
            const result = new ASTExprStructure(constructorName, []);
            result.startPos = constructorName.startPos;
            result.endPos = constructorName.endPos;
            return result;
        }
        this._match(T_LPAREN);
        if (this._currentToken.tag === T_RPAREN) {
            /* Structure with no arguments with explicit parentheses,
             * e.g. "Nil()" */
            const result = new ASTExprStructure(constructorName, []);
            const endPos = this._currentToken.startPos;
            this._match(T_RPAREN);
            result.startPos = constructorName.startPos;
            result.endPos = endPos;
            return result;
        }
        const subject = this._parseExpression();
        switch (this._currentToken.tag) {
            case T_GETS:
                if (subject.tag !== N_ExprVariable) {
                    fail$4(this._currentToken.startPos, this._currentToken.endPos, 'expected-but-found', [i18n$1('T_PIPE'), i18n$1('T_GETS')]);
                    return;
                }
                return this._parseStructure(constructorName, subject.variableName);
            case T_PIPE:
                return this._parseStructureUpdate(constructorName, subject);
            case T_COMMA:
            case T_RPAREN:
                /* Issue a specific error message to deal with a common
                 * programming error, namely calling a procedure name
                 * where an expression is expected. */
                fail$4(constructorName.startPos, constructorName.endPos, 'expected-but-found', [
                    i18n$1('expression'),
                    i18n$1('procedure call')
                ]);
                return;
            default: {
                let expected;
                if (subject.tag === N_ExprVariable) {
                    expected = toFunc$3(i18n$1('<alternative>'))([i18n$1('T_GETS'), i18n$1('T_PIPE')]);
                }
                else {
                    expected = toStr(i18n$1('T_PIPE'));
                }
                fail$4(constructorName.startPos, constructorName.endPos, 'expected-but-found', [
                    expected,
                    i18n$1(Symbol.keyFor(this._currentToken.tag))
                ]);
            }
        }
    }
    /* Parse a structure   A(x1 <- expr1, ..., xN <- exprN)
     * where N >= 1,
     * assuming that  "A(x1" has already been read.
     *
     * - constructorName and fieldName1 correspond to "A" and "x1"
     *   respectively.
     */
    _parseStructure(constructorName, fieldName1) {
        /* Read "<- expr1" */
        this._match(T_GETS);
        const value1 = this._parseExpression();
        const fieldBinding1 = new ASTFieldBinding(fieldName1, value1);
        fieldBinding1.startPos = fieldName1.startPos;
        fieldBinding1.endPos = value1.endPos;
        /* Read "x2 <- expr2, ..., xN <- exprN" (this might be empty) */
        const fieldBindings = this._parseNonEmptyDelimitedSeq(T_RPAREN, T_COMMA, [fieldBinding1], () => this._parseFieldBinding());
        /* Read ")" */
        const endPos = this._currentToken.startPos;
        this._match(T_RPAREN);
        /* Return an ExprStructure node */
        const result = new ASTExprStructure(constructorName, fieldBindings);
        result.startPos = constructorName.startPos;
        result.endPos = endPos;
        return result;
    }
    /* Parse a structure update  A(e | x1 <- expr1, ..., xN <- exprN)
     * where N >= 1,
     * assuming that "A(e" has already been read.
     *
     * constructorName and original correspond to "A" and "e"
     * respectively.
     */
    _parseStructureUpdate(constructorName, original) {
        /* Read "|" */
        this._match(T_PIPE);
        /* Read "x2 <- expr2, ..., xN <- exprN" (this might be empty) */
        const fieldBindings = this._parseDelimitedSeq(T_RPAREN, T_COMMA, () => this._parseFieldBinding());
        /* Read ")" */
        const endPos = this._currentToken.startPos;
        this._match(T_RPAREN);
        /* Return an ExprStructureUpdate node */
        const result = new ASTExprStructureUpdate(constructorName, original, fieldBindings);
        result.startPos = constructorName.startPos;
        result.endPos = endPos;
        return result;
    }
    /* Read a list
     *   [expr1, ..., exprN]
     * a range expression
     *   [first .. last]
     * or a range expression with step
     *   [first, second .. last]
     */
    _parseExprListOrRange() {
        const startPos = this._currentToken.startPos;
        this._match(T_LBRACK);
        if (this._currentToken.tag === T_RBRACK) {
            return this._parseExprListRemainder(startPos, []);
        }
        const first = this._parseExpression();
        switch (this._currentToken.tag) {
            case T_RBRACK:
                return this._parseExprListRemainder(startPos, [first]);
            case T_RANGE:
                return this._parseExprRange(startPos, first);
            case T_COMMA: {
                this._match(T_COMMA);
                const second = this._parseExpression();
                switch (this._currentToken.tag) {
                    case T_RBRACK:
                    case T_COMMA:
                        return this._parseExprListRemainder(startPos, [first, second]);
                    case T_RANGE:
                        return this._parseExprRange(startPos, first, second);
                    default:
                        fail$4(this._currentToken.startPos, this._currentToken.endPos, 'expected-but-found', [
                            toFunc$3(i18n$1('<alternative>'))([
                                i18n$1('T_COMMA'),
                                i18n$1('T_RANGE'),
                                i18n$1('T_RBRACK')
                            ]),
                            i18n$1(Symbol.keyFor(this._currentToken.tag))
                        ]);
                        return;
                }
            }
            default:
                fail$4(this._currentToken.startPos, this._currentToken.endPos, 'expected-but-found', [
                    toFunc$3(i18n$1('<alternative>'))([
                        i18n$1('T_COMMA'),
                        i18n$1('T_RANGE'),
                        i18n$1('T_RBRACK')
                    ]),
                    i18n$1(Symbol.keyFor(this._currentToken.tag))
                ]);
                return;
        }
    }
    /* Read the end of a list "[expr1, ..., exprN]" assumming we have
     * already read "[expr1, ..., exprK" up to some point K >= 1.
     * - startPos is the position of "["
     * - prefix is the list of elements we have already read
     */
    _parseExprListRemainder(startPos, prefix) {
        const elements = this._parseNonEmptyDelimitedSeq(T_RBRACK, T_COMMA, prefix, () => this._parseExpression());
        const endPos = this._currentToken.startPos;
        this._match(T_RBRACK);
        const result = new ASTExprList(elements);
        result.startPos = startPos;
        result.endPos = endPos;
        return result;
    }
    /* Read a range "[first..last]" or "[first,second..last]"
     * assumming we are left to read "..last]"
     * - startPos is the position of "[".
     * - second may be null */
    _parseExprRange(startPos, first, second) {
        this._match(T_RANGE);
        const last = this._parseExpression();
        const endPos = this._currentToken.startPos;
        this._match(T_RBRACK);
        const result = new ASTExprRange(first, second, last);
        result.startPos = startPos;
        result.endPos = endPos;
        return result;
    }
    /* Read a list of expressions separated by commas and delimited
     * by parentheses. If there is a single expression, return the
     * expression itself. If there are 0 or >=2 expressions, return
     * a tuple.
     */
    _parseExprTuple(possiblyEmpty) {
        const startPos = this._currentToken.startPos;
        this._match(T_LPAREN);
        const expressionList = this._parseExpressionSeq(T_RPAREN);
        const endPos = this._currentToken.startPos;
        this._match(T_RPAREN);
        if (!possiblyEmpty && expressionList.length === 0) {
            fail$4(startPos, endPos, 'return-tuple-cannot-be-empty', []);
        }
        let result;
        if (expressionList.length === 1) {
            result = expressionList[0];
        }
        else {
            result = new ASTExprTuple(expressionList);
        }
        result.startPos = startPos;
        result.endPos = endPos;
        return result;
    }
    /** SwitchBranch **/
    _parseSwitchBranches() {
        const branches = [];
        while (this._currentToken.tag !== T_RBRACE) {
            branches.push(this._parseSwitchBranch());
        }
        return branches;
    }
    _parseSwitchBranch() {
        const pattern = this._parsePattern();
        this._match(T_ARROW);
        const body = this._parseStmtBlock();
        const result = new ASTSwitchBranch(pattern, body);
        result.startPos = pattern.startPos;
        result.endPos = body.endPos;
        return result;
    }
    /** MatchingBranch **/
    _parseMatchingBranches() {
        const branches = [];
        while (this._currentToken.tag !== T_OTHERWISE) {
            branches.push(this._parseMatchingBranch());
        }
        this._match(T_OTHERWISE);
        return branches;
    }
    _parseMatchingBranch() {
        const body = this._parseExpression();
        switch (this._currentToken.tag) {
            case T_ON: {
                this._match(T_ON);
                const pattern = this._parsePattern();
                const result = new ASTMatchingBranch(pattern, body);
                result.startPos = body.startPos;
                result.endPos = pattern.endPos;
                return result;
            }
            case T_OTHERWISE: {
                const pattern = new ASTPatternWildcard();
                pattern.startPos = this._currentToken.startPos;
                pattern.endPos = this._currentToken.endPos;
                const result = new ASTMatchingBranch(pattern, body);
                result.startPos = body.startPos;
                result.endPos = this._currentToken.endPos;
                return result;
            }
            default:
                fail$4(this._currentToken.startPos, this._currentToken.endPos, 'expected-but-found', [
                    toFunc$3(i18n$1('<alternative>'))([i18n$1('T_ON'), i18n$1('T_OTHERWISE')]),
                    i18n$1(Symbol.keyFor(this._currentToken.tag))
                ]);
        }
    }
    /** FieldBinding **/
    _parseFieldBinding() {
        const fieldName = this._parseLowerid();
        this._match(T_GETS);
        const value = this._parseExpression();
        const result = new ASTFieldBinding(fieldName, value);
        result.startPos = fieldName.startPos;
        result.endPos = value.endPos;
        return result;
    }
    /** Helpers **/
    /* Advance to the next token */
    _nextToken() {
        this._currentToken = this._lexer.nextToken();
    }
    /* Check that the current token has the expected tag.
     * Then advance to the next token. */
    _match(tokenTag) {
        if (this._currentToken.tag !== tokenTag) {
            fail$4(this._currentToken.startPos, this._currentToken.endPos, 'expected-but-found', [
                i18n$1(Symbol.keyFor(tokenTag)),
                i18n$1(Symbol.keyFor(this._currentToken.tag))
            ]);
        }
        this._nextToken();
    }
    /* Check that the current token has the expected tag.
     * Then advance to the next token.
     * Otherwise report that any of the alternatives in the tagList
     * was expected.
     */
    _matchExpected(tokenTag, tagList) {
        if (this._currentToken.tag !== tokenTag) {
            fail$4(this._currentToken.startPos, this._currentToken.endPos, 'expected-but-found', [
                toFunc$3(i18n$1('<alternative>'))(tagList.map((tag) => i18n$1(Symbol.keyFor(tag)))),
                i18n$1(Symbol.keyFor(this._currentToken.tag))
            ]);
        }
        this._nextToken();
    }
    /* Parse a delimited list:
     *   rightDelimiter: token tag for the right delimiter
     *   separator: token tag for the separator
     *   parseElement: function that parses one element */
    _parseDelimitedSeq(rightDelimiter, separator, parseElement) {
        if (this._currentToken.tag === rightDelimiter) {
            return []; /* Empty case */
        }
        const first = parseElement();
        return this._parseNonEmptyDelimitedSeq(rightDelimiter, separator, [first], parseElement);
    }
    /* Parse a delimited list, assuming the first elements are already given.
     *   rightDelimiter: token tag for the right delimiter
     *   separator: token tag for the separator
     *   prefix: non-empty list of all the first elements (already given)
     *   parseElement: function that parses one element */
    _parseNonEmptyDelimitedSeq(rightDelimiter, separator, prefix, parseElement) {
        const list = prefix;
        while (this._currentToken.tag === separator) {
            this._match(separator);
            list.push(parseElement());
        }
        if (this._currentToken.tag !== rightDelimiter) {
            fail$4(this._currentToken.startPos, this._currentToken.endPos, 'expected-but-found', [
                toFunc$3(i18n$1('<alternative>'))([
                    i18n$1(Symbol.keyFor(separator)),
                    i18n$1(Symbol.keyFor(rightDelimiter))
                ]),
                i18n$1(Symbol.keyFor(this._currentToken.tag))
            ]);
        }
        return list;
    }
    _parseLowerid() {
        const lowerid = this._currentToken;
        this._match(T_LOWERID);
        return lowerid;
    }
    _parseUpperid() {
        const upperid = this._currentToken;
        this._match(T_UPPERID);
        return upperid;
    }
    _parseLoweridSeq() {
        return this._parseDelimitedSeq(T_RPAREN, T_COMMA, () => this._parseLowerid());
    }
    /* Parse a list of expressions delimited by the given right delimiter
     * e.g. T_RPAREN or T_RBRACK, without consuming the delimiter. */
    _parseExpressionSeq(rightDelimiter) {
        return this._parseDelimitedSeq(rightDelimiter, T_COMMA, () => this._parseExpression());
    }
}

/* eslint-disable no-underscore-dangle */
/* Opcodes are constant symbols */
const I_PushInteger = Symbol.for('I_PushInteger');
const I_PushString = Symbol.for('I_PushString');
const I_PushVariable = Symbol.for('I_PushVariable');
const I_SetVariable = Symbol.for('I_SetVariable');
const I_UnsetVariable = Symbol.for('I_UnsetVariable');
const I_Label = Symbol.for('I_Label');
const I_Jump = Symbol.for('I_Jump');
const I_JumpIfFalse = Symbol.for('I_JumpIfFalse');
const I_JumpIfStructure = Symbol.for('I_JumpIfStructure');
const I_JumpIfTuple = Symbol.for('I_JumpIfTuple');
const I_Call = Symbol.for('I_Call');
const I_Return = Symbol.for('I_Return');
const I_MakeTuple = Symbol.for('I_MakeTuple');
const I_MakeList = Symbol.for('I_MakeList');
const I_MakeStructure = Symbol.for('I_MakeStructure');
const I_UpdateStructure = Symbol.for('I_UpdateStructure');
const I_ReadTupleComponent = Symbol.for('I_ReadTupleComponent');
const I_ReadStructureField = Symbol.for('I_ReadStructureField');
const I_ReadStructureFieldPop = Symbol.for('I_ReadStructureFieldPop');
const I_Add = Symbol.for('I_Add');
const I_Dup = Symbol.for('I_Dup');
const I_Pop = Symbol.for('I_Pop');
const I_PrimitiveCall = Symbol.for('I_PrimitiveCall');
const I_SaveState = Symbol.for('I_SaveState');
const I_RestoreState = Symbol.for('I_RestoreState');
const I_TypeCheck = Symbol.for('I_TypeCheck');
class Code {
    constructor(instructions) {
        this._instructions = instructions;
    }
    toString() {
        const res = [];
        for (const instruction of this._instructions) {
            res.push(instruction.toString());
        }
        return res.join('\n');
    }
    produce(instruction) {
        this._instructions.push(instruction);
    }
    /* Return the instruction at the given location */
    at(ip) {
        if (ip >= 0 && ip < this._instructions.length) {
            return this._instructions[ip];
        }
        else {
            throw Error('Code: instruction pointer out of range.');
        }
    }
    /* Return a dictionary mapping label names to their corresponding
     * instruction pointers. */
    labelTargets() {
        const labelTargets = {};
        for (let i = 0; i < this._instructions.length; i++) {
            if (this._instructions[i].opcode === I_Label) {
                const label = this._instructions[i].label;
                if (label in labelTargets) {
                    throw Error('Code: label "' + label + '" is repeated.');
                }
                labelTargets[label] = i;
            }
        }
        return labelTargets;
    }
}
function argToString(arg) {
    if (arg instanceof Array) {
        const res = [];
        for (const elem of arg) {
            res.push(argToString(elem));
        }
        return '[' + res.join(', ') + ']';
    }
    else {
        return arg.toString();
    }
}
class Instruction {
    constructor(opcode, args) {
        this._opcode = opcode;
        this._args = args;
        this._startPos = UnknownPosition;
        this._endPos = UnknownPosition;
    }
    toString() {
        const opcode = Symbol.keyFor(this._opcode).substring(2);
        const sargs = [];
        for (const arg of this._args) {
            sargs.push(argToString(arg));
        }
        return '  ' + opcode + ' ' + sargs.join(', ');
    }
    get opcode() {
        return this._opcode;
    }
    get args() {
        return this._args;
    }
    set startPos(position) {
        this._startPos = position;
    }
    get startPos() {
        return this._startPos;
    }
    set endPos(position) {
        this._endPos = position;
    }
    get endPos() {
        return this._endPos;
    }
}
/* Push a constant on the stack. */
class IPushInteger extends Instruction {
    constructor(number) {
        super(I_PushInteger, [number]);
    }
    get number() {
        return this._args[0];
    }
}
class IPushString extends Instruction {
    constructor(string) {
        super(I_PushString, [string]);
    }
    get string() {
        return this._args[0];
    }
}
/* Push a local index/variable/parameter on the stack. */
class IPushVariable extends Instruction {
    constructor(variableName) {
        super(I_PushVariable, [variableName]);
    }
    get variableName() {
        return this._args[0];
    }
}
/* Set a local index/variable/parameter to the value on the top of the stack. */
class ISetVariable extends Instruction {
    constructor(variableName) {
        super(I_SetVariable, [variableName]);
    }
    get variableName() {
        return this._args[0];
    }
}
/* Unset a local index/variable/parameter.
 * This should be used to avoid the variable being used after the end
 * of its scope.
 *
 * E.g. "i" should have no value after the end of the foreach:
 *
 *   foreach i in [1,2,3] {
 *   }
 *   x := i
 */
class IUnsetVariable extends Instruction {
    constructor(variableName) {
        super(I_UnsetVariable, [variableName]);
    }
    get variableName() {
        return this._args[0];
    }
}
/* Pseudo-instruction to mark the target of a jump. */
class ILabel extends Instruction {
    constructor(label) {
        super(I_Label, [label]);
    }
    toString() {
        return this.label + ':';
    }
    get label() {
        return this._args[0];
    }
}
/* Unconditional jump. */
class IJump extends Instruction {
    constructor(targetLabel) {
        super(I_Jump, [targetLabel]);
    }
    get targetLabel() {
        return this._args[0];
    }
}
/* Jump if the top of the stack is False.
 * Pops the top of the stack. */
class IJumpIfFalse extends Instruction {
    constructor(targetLabel) {
        super(I_JumpIfFalse, [targetLabel]);
    }
    get targetLabel() {
        return this._args[0];
    }
}
/* Jump if the top of the stack is a structure built using the given
 * constructor. Does NOT pop the top of the stack. */
class IJumpIfStructure extends Instruction {
    constructor(constructorName, targetLabel) {
        super(I_JumpIfStructure, [constructorName, targetLabel]);
    }
    get constructorName() {
        return this._args[0];
    }
    get targetLabel() {
        return this._args[1];
    }
}
/* Jump if the top of the stack is an n-tuple of the given size.
 * Does NOT pop the top of the stack. */
class IJumpIfTuple extends Instruction {
    constructor(size, targetLabel) {
        super(I_JumpIfTuple, [size, targetLabel]);
    }
    get size() {
        return this._args[0];
    }
    get targetLabel() {
        return this._args[1];
    }
}
/* Call a subroutine (procedure or function).
 * The arguments are expected to be located in the stack
 * with the last one at the top.
 *
 * The arguments are popped from the current frame and pushed
 * onto the new frame.
 */
class ICall extends Instruction {
    constructor(targetLabel, nargs) {
        super(I_Call, [targetLabel, nargs]);
    }
    get targetLabel() {
        return this._args[0];
    }
    get nargs() {
        return this._args[1];
    }
}
/* Return from a routine to the caller.
 * If returning a value (from a function or program),
 * it must be on the top of the stack. */
class IReturn extends Instruction {
    constructor() {
        super(I_Return, []);
    }
}
/* Make a tuple of the given size.
 * The components are expected to be located in the stack
 * with the last one at the top. */
class IMakeTuple extends Instruction {
    constructor(size) {
        super(I_MakeTuple, [size]);
    }
    get size() {
        return this._args[0];
    }
}
/* Make a list of the given size.
 * The elements are expected to be located in the stack
 * with the last one at the top. */
class IMakeList extends Instruction {
    constructor(size) {
        super(I_MakeList, [size]);
    }
    get size() {
        return this._args[0];
    }
}
/* Make a structure using the given constructor and the given fields.
 * The values of the fields are expected to be located in the stack
 * with the last one at the top. */
class IMakeStructure extends Instruction {
    constructor(typeName, constructorName, fieldNames) {
        super(I_MakeStructure, [typeName, constructorName, fieldNames]);
    }
    get typeName() {
        return this._args[0];
    }
    get constructorName() {
        return this._args[1];
    }
    get fieldNames() {
        return this._args[2];
    }
}
/* Update a structure built using the given constructor with the given
 * fields.
 * The stack should have a structure built using the given constructor,
 * followed by the values of the fields that are expected.
 * The last field should be at the top. */
class IUpdateStructure extends Instruction {
    constructor(typeName, constructorName, fieldNames) {
        super(I_UpdateStructure, [typeName, constructorName, fieldNames]);
    }
    get typeName() {
        return this._args[0];
    }
    get constructorName() {
        return this._args[1];
    }
    get fieldNames() {
        return this._args[2];
    }
}
/* Read the n-th component from the tuple at the top of the stack.
 * Does not pop the tuple. */
class IReadTupleComponent extends Instruction {
    constructor(index) {
        super(I_ReadTupleComponent, [index]);
    }
    get index() {
        return this._args[0];
    }
}
/* Read the given field from the structure at the top of the stack.
 * Does not pop the structure. */
class IReadStructureField extends Instruction {
    constructor(fieldName) {
        super(I_ReadStructureField, [fieldName]);
    }
    get fieldName() {
        return this._args[0];
    }
}
/* Read the given field from the structure at the top of the stack.
 * Pop the structure. */
class IReadStructureFieldPop extends Instruction {
    constructor(fieldName) {
        super(I_ReadStructureFieldPop, [fieldName]);
    }
    get fieldName() {
        return this._args[0];
    }
}
/* Add the topmost elements of the stack (used mostly for testing/debugging) */
class IAdd extends Instruction {
    constructor() {
        super(I_Add, []);
    }
}
/* Duplicate the top of the stack (there should be at least one element) */
class IDup extends Instruction {
    constructor() {
        super(I_Dup, []);
    }
}
/* Pop the top of the stack (there should be at least one element) */
class IPop extends Instruction {
    constructor() {
        super(I_Pop, []);
    }
}
/* Call a primitive function.
 *
 * The arguments are expected to be located in the stack
 * with the last one at the top.
 *
 * Note: the compiler relies on various primitive functions.
 * For example, the operation to make a range is a primitive
 * function:
 *
 *   function _makeRange(start, end)
 *
 * So is the function that checks whether the top of the stack is a list,
 * etc. (required to compile a "foreach"), and so on.
 */
class IPrimitiveCall extends Instruction {
    constructor(primitiveName, nargs) {
        super(I_PrimitiveCall, [primitiveName, nargs]);
    }
    get primitiveName() {
        return this._args[0];
    }
    get nargs() {
        return this._args[1];
    }
}
/* Save the global state (when entering a function) */
class ISaveState extends Instruction {
    constructor() {
        super(I_SaveState, []);
    }
}
/* Restore the global state (when leaving a function) */
class IRestoreState extends Instruction {
    constructor() {
        super(I_RestoreState, []);
    }
}
/* Check that the top of the stack has the given type.
 * Does not pop the top of the stack. */
class ITypeCheck extends Instruction {
    constructor(type) {
        super(I_TypeCheck, [type]);
    }
    get type() {
        return this._args[0];
    }
}

/* eslint-disable @typescript-eslint/explicit-function-return-type */
/* eslint-disable quote-props */
const keyword$1 = (palabra) => 'la palabra clave "' + palabra + '"';
function pluralize$1(n, singular, plural) {
    if (n === 0) {
        return 'ningún ' + singular;
    }
    else if (n === 1) {
        return 'un ' + singular;
    }
    else {
        return n.toString() + ' ' + plural;
    }
}
// Only for typing purposes
// eslint-disable-next-line @typescript-eslint/ban-types
const toFunc$1 = (x) => x;
function ordinalNumber(n) {
    const units = [
        '',
        'primer',
        'segundo',
        'tercer',
        'cuarto',
        'quinto',
        'sexto',
        'séptimo',
        'octavo',
        'noveno'
    ];
    if (n >= 1 && n <= 9) {
        return units[n];
    }
    else {
        return '#' + n.toString();
    }
}
function describeType(type) {
    if (type.isInteger()) {
        return ['m', 'número', 'números'];
    }
    else if (type.isBoolean()) {
        return ['m', 'booleano', 'booleanos'];
    }
    else if (type.isColor()) {
        return ['m', 'color', 'colores'];
    }
    else if (type.isDirection()) {
        return ['f', 'dirección', 'direcciones'];
    }
    else if (type.isList() && type.contentType.isAny()) {
        return ['f', 'lista', 'listas'];
    }
    else if (type.isList()) {
        const description = describeType(type.contentType);
        if (description === undefined) {
            return undefined;
        }
        else {
            const plural = description[2];
            return ['f', 'lista de ' + plural, 'listas de ' + plural];
        }
    }
    else {
        return undefined;
    }
}
function describeTypeSingular(type) {
    const description = describeType(type);
    if (description === undefined) {
        return type.toString();
    }
    else {
        const singular = description[1];
        return singular;
    }
}
function typeAsNoun(type) {
    const description = describeType(type);
    if (description === undefined) {
        return 'un valor de tipo ' + type.toString();
    }
    else {
        const gender = description[0];
        const singular = description[1];
        if (gender === 'm') {
            return 'un ' + singular;
        }
        else {
            return 'una ' + singular;
        }
    }
}
function typeAsQualifierSingular(type) {
    const description = describeType(type);
    if (description === undefined) {
        return 'de tipo ' + type.toString();
    }
    else {
        const gender = description[0];
        const singular = description[1];
        if (gender === 'm') {
            return 'un ' + singular;
        }
        else {
            return 'una ' + singular;
        }
    }
}
function typeAsQualifierPlural(type) {
    const description = describeType(type);
    if (description === undefined) {
        return 'de tipo ' + type.toString();
    }
    else {
        const gender = description[0];
        const plural = description[2];
        if (gender === 'm') {
            return plural;
        }
        else {
            return plural;
        }
    }
}
function listOfTypes(types) {
    const typeStrings = [];
    for (const type of types) {
        typeStrings.push(describeTypeSingular(type));
    }
    return typeStrings.join(', ');
}
function openingDelimiterName(delimiter) {
    if (delimiter === '(' || delimiter === ')') {
        return 'un paréntesis abierto "("';
    }
    else if (delimiter === '[' || delimiter === ']') {
        return 'un corchete abierto "["';
    }
    else if (delimiter === '{' || delimiter === '}') {
        return 'una llave abierta "{"';
    }
    else {
        return delimiter;
    }
}
function formatTypes(string, type1, type2) {
    let result = '';
    for (let i = 0; i < string.length; i++) {
        if (string[i] === '%' && i + 1 < string.length) {
            if (string[i + 1] === '%') {
                result += '%';
                i++;
            }
            else if (string[i + 1] === '1') {
                result += typeAsNoun(type1);
                i++;
            }
            else if (string[i + 1] === '2') {
                result += typeAsNoun(type2);
                i++;
            }
            else {
                result += '%';
            }
        }
        else {
            result += string[i];
        }
    }
    return result;
}
// eslint-disable-next-line @typescript-eslint/ban-types
const LOCALE_ES = {
    /* Descriptions of syntactic constructions and tokens */
    definition: 'una definición (de programa, función, procedimiento, o tipo)',
    pattern: 'un patrón (comodín "_", constructor aplicado a variables, o tupla)',
    statement: 'un comando',
    expression: 'una expresión',
    'procedure call': 'una invocación a un procedimiento',
    'field name': 'el nombre de un campo',
    T_EOF: 'el final del archivo',
    T_NUM: 'un número',
    T_STRING: 'una cadena (string)',
    T_UPPERID: 'un identificador con mayúsculas',
    T_LOWERID: 'un identificador con minúsculas',
    T_PROGRAM: keyword$1('program'),
    T_INTERACTIVE: keyword$1('interactive'),
    T_PROCEDURE: keyword$1('procedure'),
    T_FUNCTION: keyword$1('function'),
    T_RETURN: keyword$1('return'),
    T_IF: keyword$1('if'),
    T_THEN: keyword$1('then'),
    T_ELSE: keyword$1('else'),
    T_REPEAT: keyword$1('repeat'),
    T_FOREACH: keyword$1('foreach'),
    T_IN: keyword$1('in'),
    T_WHILE: keyword$1('while'),
    T_SWITCH: keyword$1('switch'),
    T_TO: keyword$1('to'),
    T_LET: keyword$1('let'),
    T_NOT: keyword$1('not'),
    T_DIV: keyword$1('div'),
    T_MOD: keyword$1('mod'),
    T_TYPE: keyword$1('type'),
    T_IS: keyword$1('is'),
    T_CHOOSE: keyword$1('choose'),
    T_WHEN: keyword$1('when'),
    T_OTHERWISE: keyword$1('otherwise'),
    T_MATCHING: keyword$1('matching'),
    T_SELECT: keyword$1('select'),
    T_ON: keyword$1('on'),
    T_RECORD: keyword$1('record'),
    T_VARIANT: keyword$1('variant'),
    T_CASE: keyword$1('case'),
    T_FIELD: keyword$1('field'),
    T_UNDERSCORE: 'un guión bajo ("_")',
    T_LPAREN: 'un paréntesis izquierdo ("(")',
    T_RPAREN: 'un paréntesis derecho (")")',
    T_LBRACE: 'una llave izquierda ("{")',
    T_RBRACE: 'una llave derecha ("}")',
    T_LBRACK: 'un corchete izquierdo ("[")',
    T_RBRACK: 'un corchete derecho ("]")',
    T_COMMA: 'una coma (",")',
    T_SEMICOLON: 'un punto y coma (";")',
    T_RANGE: 'un separador de rango ("..")',
    T_GETS: 'una flecha hacia la izquierda ("<-")',
    T_PIPE: 'una barra vertical ("|")',
    T_ARROW: 'una flecha ("->")',
    T_ASSIGN: 'un operador de asignación (":=")',
    T_EQ: 'una comparación por igualdad ("==")',
    T_NE: 'una comparación por desigualdad ("/=")',
    T_LE: 'un menor o igual ("<=")',
    T_GE: 'un mayor o igual (">=")',
    T_LT: 'un menor estricto ("<")',
    T_GT: 'un mayor estricto (">")',
    T_AND: 'el "y" lógico ("&&")',
    T_OR: 'el "o" lógico ("||")',
    T_CONCAT: 'el operador de concatenación de listas ("++")',
    T_PLUS: 'el operador de suma ("+")',
    T_MINUS: 'el operador de resta ("-")',
    T_TIMES: 'el operador de producto ("*")',
    T_POW: 'el operador de potencia ("^")',
    /* Local name categories */
    LocalVariable: 'variable',
    LocalIndex: 'índice',
    LocalParameter: 'parámetro',
    /* Descriptions of value types */
    V_Integer: 'un número',
    V_String: 'una cadena',
    V_Tuple: 'una tupla',
    V_List: 'una lista',
    V_Structure: 'una estructura',
    /* Lexer */
    'errmsg:unclosed-multiline-comment': 'El comentario se abre pero nunca se cierra.',
    'errmsg:unclosed-string-constant': 'La comilla que abre no tiene una comilla que cierra correspondiente.',
    // eslint-disable-next-line max-len
    'errmsg:numeric-constant-should-not-have-leading-zeroes': `Las constantes numéricas no se pueden escribir con ceros a la izquierda.`,
    // eslint-disable-next-line max-len
    'errmsg:identifier-must-start-with-alphabetic-character': `Los identificadores deben empezar con un caracter alfabético (a...z,A...Z).`,
    'errmsg:unknown-token': (symbol) => 'Símbolo desconocido en la entrada: "' + symbol + '".',
    'warning:empty-pragma': 'Directiva pragma vacía.',
    'warning:unknown-pragma': (pragmaName) => 'Directiva pragma desconocida: "' + pragmaName + '".',
    'errmsg:unmatched-opening-delimiter': (delimiter) => 'Se encontró ' + openingDelimiterName(delimiter) + ' pero nunca se cierra.',
    'errmsg:unmatched-closing-delimiter': (delimiter) => 'Se encontró un "' +
        delimiter +
        '" ' +
        'pero no había ' +
        openingDelimiterName(delimiter) +
        '.',
    'errmsg:unknown-language-option': (option) => 'Opción desconocida. "' + option + '".',
    /* Parser */
    'errmsg:empty-source': 'El programa está vacío.',
    'errmsg:expected-but-found': (expected, found) => `Se esperaba ${expected}. Se encontró: ${found}.`,
    'errmsg:pattern-number-cannot-be-negative-zero': 'El patrón numérico no puede ser "-0".',
    'errmsg:return-tuple-cannot-be-empty': 'El return tiene que devolver algo.',
    'errmsg:pattern-tuple-cannot-be-singleton': 'El patrón para una tupla no puede tener una sola componente. ' +
        'Las tuplas tienen 0, 2, 3, o más componentes, pero no 1.',
    'errmsg:assignment-tuple-cannot-be-singleton': 'La asignación a una tupla no puede constar de una sola componente. ' +
        'Las tuplas tienen 0, 2, 3, o más componentes, pero no 1.',
    'errmsg:operators-are-not-associative': (op1, op2) => 'La expresión usa ' +
        op1 +
        ' y ' +
        op2 +
        ', pero estos operadores no se pueden asociar. ' +
        'Quizás faltan paréntesis.',
    'errmsg:obsolete-tuple-assignment': 'Se esperaba un comando pero se encontró un paréntesis izquierdo. ' +
        'Nota: la sintaxis de asignación de tuplas "(x1, ..., xN) := y" ' +
        'está obsoleta. Usar "let (x1, ..., xN) := y".',
    /* Linter */
    'errmsg:program-already-defined': (pos1, pos2) => 'Ya había un programa definido en ' +
        pos1 +
        '.\n' +
        'No se puede definir un programa en ' +
        pos2 +
        '.',
    'errmsg:procedure-already-defined': (name, pos1, pos2) => 'El procedimiento "' +
        name +
        '" está definido dos veces: ' +
        'en ' +
        pos1 +
        ' y en ' +
        pos2 +
        '.',
    'errmsg:function-already-defined': (name, pos1, pos2) => 'La función "' +
        name +
        '" está definida dos veces: ' +
        'en ' +
        pos1 +
        ' y en ' +
        pos2 +
        '.',
    'errmsg:type-already-defined': (name, pos1, pos2) => `El tipo "${name}" está definido dos veces: en ${pos1} y en ${pos2}.`,
    'errmsg:constructor-already-defined': (name, pos1, pos2) => 'El constructor "' +
        name +
        '" está definido dos veces: ' +
        'en ' +
        pos1 +
        ' y en ' +
        pos2 +
        '.',
    'errmsg:repeated-field-name': (constructorName, fieldName) => 'El campo "' +
        fieldName +
        '" no puede estar repetido ' +
        'para el constructor "' +
        constructorName +
        '".',
    'errmsg:function-and-field-cannot-have-the-same-name': (name, posFunction, posField) => 'El nombre "' +
        name +
        '" se usa ' +
        'para una función en ' +
        posFunction +
        ' y ' +
        'para un campo en ' +
        posField +
        '.',
    'errmsg:source-should-have-a-program-definition': 
    /* Note: the code may actually be completely empty, but
     * we avoid this technicality since the message could be
     * confusing. */
    'El código debe tener una definición de "program { ... }".',
    'errmsg:procedure-should-not-have-return': (name) => `El procedimiento "${name}" no debería tener un comando "return".`,
    'errmsg:function-should-have-return': (name) => 'La función "' + name + '" debería tener un comando "return".',
    'errmsg:return-statement-not-allowed-here': 'El comando "return" solo puede aparecer como el último comando ' +
        'de una función o como el último comando del programa.',
    'errmsg:local-name-conflict': (name, oldCat, oldPos, newCat, newPos) => 'Conflicto de nombres: "' +
        name +
        '" se usa dos veces: ' +
        'como ' +
        oldCat +
        ' en ' +
        oldPos +
        ', y ' +
        'como ' +
        newCat +
        ' en ' +
        newPos +
        '.',
    'errmsg:repeated-variable-in-tuple-assignment': (name) => `La variable "${name}" está repetida en la asignación de tuplas.`,
    'errmsg:constructor-used-as-procedure': (name, type) => 'El procedimiento "' +
        name +
        '" no está definido. ' +
        'El nombre "' +
        name +
        '" es el nombre de un constructor ' +
        'del tipo "' +
        type +
        '".',
    'errmsg:undefined-procedure': (name) => 'El procedimiento "' + name + '" no está definido.',
    'errmsg:undefined-function': (name) => 'La función "' + name + '" no está definida.',
    'errmsg:procedure-arity-mismatch': (name, expected, received) => '"El procedimiento "' +
        name +
        '" espera recibir ' +
        toFunc$1(LOCALE_ES['<n>-parameters'])(expected) +
        ' pero se lo invoca con ' +
        toFunc$1(LOCALE_ES['<n>-arguments'])(received) +
        '.',
    'errmsg:function-arity-mismatch': (name, expected, received) => 'La función "' +
        name +
        '" espera recibir ' +
        toFunc$1(LOCALE_ES['<n>-parameters'])(expected) +
        ' pero se la invoca con ' +
        toFunc$1(LOCALE_ES['<n>-arguments'])(received) +
        '.',
    'errmsg:structure-pattern-arity-mismatch': (name, expected, received) => 'El constructor "' +
        name +
        '" tiene ' +
        toFunc$1(LOCALE_ES['<n>-fields'])(expected) +
        ' pero el patrón tiene ' +
        toFunc$1(LOCALE_ES['<n>-parameters'])(received) +
        '.',
    'errmsg:type-used-as-constructor'(name, constructorNames) {
        let msg;
        if (constructorNames.length === 0) {
            msg = '(no tiene constructores).';
        }
        else if (constructorNames.length === 1) {
            msg = '(tiene un constructor: ' + constructorNames[0] + ').';
        }
        else {
            msg = '(sus constructores son: ' + constructorNames.join(', ') + ').';
        }
        return ('El constructor "' +
            name +
            '" no está definido. ' +
            'El nombre "' +
            name +
            '" es el nombre de un tipo ' +
            msg);
    },
    'errmsg:procedure-used-as-constructor': (name) => 'El constructor "' +
        name +
        '" no está definido. ' +
        'El nombre "' +
        name +
        '" es el nombre de un procedimiento.',
    'errmsg:undeclared-constructor': (name) => 'El constructor "' + name + '" no está definido.',
    'errmsg:wildcard-pattern-should-be-last': 'El comodín "_" debe estar en la última rama.',
    'errmsg:variable-pattern-should-be-last': (name) => 'El patrón variable "' + name + '" tiene debe estar en la última rama.',
    'errmsg:numeric-pattern-repeats-number': (number) => 'Hay dos ramas distintas para el número "' + number + '".',
    'errmsg:structure-pattern-repeats-constructor': (name) => 'Hay dos ramas distintas para el constructor "' + name + '".',
    'errmsg:structure-pattern-repeats-tuple-arity': (arity) => 'Hay dos ramas distintas para las tuplas de ' + arity.toString() + ' componentes.',
    'errmsg:structure-pattern-repeats-timeout': 'Hay dos ramas distintas para el TIMEOUT.',
    'errmsg:pattern-does-not-match-type': (expectedType, patternType) => 'Los patrones tienen que ser todos del mismo tipo. ' +
        'El patrón debería ser de tipo ' +
        expectedType +
        'pero es de tipo ' +
        patternType +
        '.',
    'errmsg:patterns-in-interactive-program-must-be-events': 'Los patrones de un "interactive program" deben ser eventos.',
    'errmsg:patterns-in-interactive-program-cannot-be-variables': 'El patrón no puede ser una variable.',
    'errmsg:patterns-in-switch-must-not-be-events': 'El patrón no puede ser un evento.',
    'errmsg:structure-construction-repeated-field': (constructorName, fieldName) => 'El campo "' +
        fieldName +
        '" está repetido en ' +
        'la instanciación del constructor "' +
        constructorName +
        '".',
    'errmsg:structure-construction-invalid-field': (constructorName, fieldName) => 'El campo "' +
        fieldName +
        '" no es un campo válido ' +
        'para el constructor "' +
        constructorName +
        '".',
    'errmsg:structure-construction-missing-field': (constructorName, fieldName) => 'Falta darle valor al campo "' +
        fieldName +
        '" ' +
        'del constructor "' +
        constructorName +
        '".',
    'errmsg:structure-construction-cannot-be-an-event': (constructorName) => 'El constructor "' +
        constructorName +
        '" corresponde a un ' +
        'evento, y solamente se puede manejar implícitamente ' +
        'en un programa interactivo (el usuario no puede construir ' +
        'instancias).',
    'errmsg:forbidden-extension-destructuring-foreach': 'El índice de la repetición indexada debe ser un identificador.',
    ['errmsg:forbidden-extension-allow-recursion']: (cycle) => {
        const msg = [];
        for (const call of cycle) {
            msg.push('  ' +
                call.caller +
                ' llama a ' +
                call.callee +
                ' (' +
                call.location.startPos.filename.toString() +
                ':' +
                call.location.startPos.line.toString() +
                ':' +
                call.location.startPos.column.toString() +
                ')');
        }
        return ('La recursión está deshabilitada. ' +
            'Hay un ciclo en las invocaciones:\n' +
            msg.join('\n'));
    },
    'errmsg:patterns-in-foreach-must-not-be-events': 'El patrón de un foreach no puede ser un evento.',
    /* Runtime errors (virtual machine) */
    'errmsg:ellipsis': 'El programa todavía no está completo.',
    'errmsg:undefined-variable': (variableName) => 'La variable "' + variableName + '" no está definida.',
    'errmsg:too-few-arguments': (routineName) => 'Faltan argumentos para "' + routineName + '".',
    'errmsg:expected-structure-but-got': (constructorName, valueTag) => 'Se esperaba una estructura construida ' +
        'con el constructor "' +
        constructorName +
        '", ' +
        'pero se recibió ' +
        valueTag +
        '.',
    'errmsg:expected-constructor-but-got': (constructorNameExpected, constructorNameReceived) => 'Se esperaba una estructura construida ' +
        'con el constructor "' +
        constructorNameExpected +
        '", ' +
        'pero el constructor recibido es ' +
        constructorNameReceived +
        '".',
    'errmsg:incompatible-types-on-assignment': (variableName, oldType, newType) => 'La variable "' +
        variableName +
        '" ' +
        'contenía ' +
        typeAsNoun(oldType) +
        ', ' +
        'no se le puede asignar ' +
        typeAsNoun(newType) +
        '".',
    'errmsg:incompatible-types-on-list-creation': (index, oldType, newType) => 'Todos los elementos de una lista deben ser del mismo tipo. ' +
        'Los elementos son ' +
        typeAsQualifierPlural(oldType) +
        ', ' +
        'pero el elemento en la posición ' +
        index.toString() +
        ' ' +
        'es ' +
        typeAsQualifierSingular(newType) +
        '.',
    'errmsg:incompatible-types-on-structure-update': (fieldName, oldType, newType) => 'El campo "' +
        fieldName +
        '" es ' +
        typeAsQualifierSingular(oldType) +
        '. ' +
        'No se lo puede actualizar con ' +
        typeAsNoun(newType) +
        '.',
    'errmsg:expected-tuple-value-but-got': (receivedType) => 'Se esperaba una tupla pero se recibió ' + typeAsNoun(receivedType) + '.',
    'errmsg:tuple-component-out-of-bounds': (size, index) => 'Índice fuera de rango. ' +
        'La tupla es de tamaño ' +
        size.toString() +
        ' y ' +
        'el índice es ' +
        index.toString() +
        '.',
    'errmsg:expected-structure-value-but-got': (receivedType) => 'Se esperaba una estructura pero se recibió ' + typeAsNoun(receivedType) + '.',
    'errmsg:structure-field-not-present': (fieldNames, missingFieldName) => 'La estructura no tiene un campo "' +
        missingFieldName +
        '". ' +
        'Los campos son: [' +
        fieldNames.join(', ') +
        '].',
    'errmsg:primitive-does-not-exist': (primitiveName) => `La operación primitiva "${primitiveName}" no existe o no está disponible.`,
    'errmsg:primitive-arity-mismatch': (name, expected, received) => 'La operación "' +
        name +
        '" espera recibir ' +
        toFunc$1(LOCALE_ES['<n>-parameters'])(expected) +
        ' pero se la invoca con ' +
        toFunc$1(LOCALE_ES['<n>-arguments'])(received) +
        '.',
    'errmsg:primitive-argument-type-mismatch'(name, parameterIndex, numArgs, expectedType, receivedType) {
        let msg = 'El ';
        if (numArgs > 1) {
            msg += ordinalNumber(parameterIndex) + ' ';
        }
        msg += 'parámetro ';
        msg += 'de "' + name + '" ';
        msg += 'debería ser ' + typeAsQualifierSingular(expectedType) + ' ';
        msg += 'pero es ' + typeAsQualifierSingular(receivedType) + '.';
        return msg;
    },
    'errmsg:expected-value-of-type-but-got': (expectedType, receivedType) => 'Se esperaba ' +
        typeAsNoun(expectedType) +
        ' ' +
        'pero se recibió ' +
        typeAsNoun(receivedType) +
        '.',
    'errmsg:expected-value-of-some-type-but-got': (expectedTypes, receivedType) => 'Se esperaba un valor de alguno de los siguientes tipos: ' +
        listOfTypes(expectedTypes) +
        '. ' +
        'Pero se recibió ' +
        typeAsNoun(receivedType) +
        '.',
    'errmsg:expected-values-to-have-compatible-types': (type1, type2) => 'Los tipos de las expresiones no coinciden: ' +
        'la primera es ' +
        typeAsQualifierSingular(type1) +
        ' ' +
        'y la segunda es ' +
        typeAsQualifierSingular(type2) +
        '.',
    'errmsg:switch-does-not-match': 'El valor analizado no coincide con ninguna de las ramas del switch.',
    'errmsg:foreach-pattern-does-not-match': 'El elemento no coincide con el patrón esperado por el foreach.',
    'errmsg:cannot-divide-by-zero': 'No se puede dividir por cero.',
    'errmsg:negative-exponent': 'El exponente de la potencia no puede ser negativo.',
    'errmsg:list-cannot-be-empty': 'La lista no puede ser vacía.',
    'errmsg:timeout': (millisecs) => 'La ejecución del programa demoró más de ' + millisecs.toString() + 'ms.',
    /* Typecheck */
    'errmsg:typecheck-failed': (errorMessage, type1, type2) => formatTypes(errorMessage, type1, type2),
    /* Board operations */
    'errmsg:cannot-move-to': (dirName) => 'No se puede mover hacia la dirección ' + dirName + ': cae afuera del tablero.',
    'errmsg:cannot-remove-stone': (dirName) => 'No se puede sacar una bolita de color ' + dirName + ': no hay bolitas de ese color.',
    /* Runtime */
    'TYPE:Integer': 'Number',
    'TYPE:String': 'String',
    'TYPE:Tuple': '',
    'TYPE:List': 'List',
    'TYPE:Event': 'Event',
    'CONS:INIT': 'INIT',
    'CONS:TIMEOUT': 'TIMEOUT',
    'TYPE:Bool': 'Bool',
    'CONS:False': 'False',
    'CONS:True': 'True',
    'TYPE:Color': 'Color',
    'CONS:Color0': 'Azul',
    'CONS:Color1': 'Negro',
    'CONS:Color2': 'Rojo',
    'CONS:Color3': 'Verde',
    'TYPE:Dir': 'Dir',
    'CONS:Dir0': 'Norte',
    'CONS:Dir1': 'Este',
    'CONS:Dir2': 'Sur',
    'CONS:Dir3': 'Oeste',
    'PRIM:TypeCheck': 'TypeCheck',
    'PRIM:BOOM': 'BOOM',
    'PRIM:boom': 'boom',
    'PRIM:PutStone': 'Poner',
    'PRIM:RemoveStone': 'Sacar',
    'PRIM:Move': 'Mover',
    'PRIM:GoToEdge': 'IrAlBorde',
    'PRIM:EmptyBoardContents': 'VaciarTablero',
    'PRIM:numStones': 'nroBolitas',
    'PRIM:anyStones': 'hayBolitas',
    'PRIM:canMove': 'puedeMover',
    'PRIM:next': 'siguiente',
    'PRIM:prev': 'previo',
    'PRIM:opposite': 'opuesto',
    'PRIM:minBool': 'minBool',
    'PRIM:maxBool': 'maxBool',
    'PRIM:minColor': 'minColor',
    'PRIM:maxColor': 'maxColor',
    'PRIM:minDir': 'minDir',
    'PRIM:maxDir': 'maxDir',
    'PRIM:isEmpty': 'esVacía',
    'PRIM:head': 'primero',
    'PRIM:tail': 'sinElPrimero',
    'PRIM:oldTail': 'resto',
    'PRIM:init': 'comienzo',
    'PRIM:last': 'último',
    /* Helpers */
    '<alternative>': (strings) => 'alguna de las siguientes alternativas:\n' +
        strings.map((s) => '  ' + s).join('\n'),
    '<position>': (filename, line, column) => filename + ':' + line.toString() + ':' + column.toString(),
    '<n>-parameters': (n) => pluralize$1(n, 'parámetro', 'parámetros'),
    '<n>-arguments': (n) => pluralize$1(n, 'argumento', 'argumentos'),
    '<n>-fields': (n) => pluralize$1(n, 'campo', 'campos'),
    '<pattern-type>'(patternType) {
        if (patternType === 'Event') {
            return 'evento del programa interactivo';
        }
        else if (patternType.substring(0, 7) === '_TUPLE_') {
            return 'tupla de ' + patternType.substring(7) + ' componentes';
        }
        else {
            return patternType;
        }
    }
};

const LOCALE_EN = {};
for (const key in LOCALE_ES) {
    LOCALE_EN[key] = LOCALE_ES[key];
}
LOCALE_EN['TYPE:Color'] = 'Color';
LOCALE_EN['CONS:Color0'] = 'Blue';
LOCALE_EN['CONS:Color1'] = 'Black';
LOCALE_EN['CONS:Color2'] = 'Red';
LOCALE_EN['CONS:Color3'] = 'Green';
LOCALE_EN['TYPE:Dir'] = 'Dir';
LOCALE_EN['CONS:Dir0'] = 'North';
LOCALE_EN['CONS:Dir1'] = 'East';
LOCALE_EN['CONS:Dir2'] = 'South';
LOCALE_EN['CONS:Dir3'] = 'West';
LOCALE_EN['PRIM:PutStone'] = 'Drop';
LOCALE_EN['PRIM:RemoveStone'] = 'Grab';
LOCALE_EN['PRIM:Move'] = 'Move';
LOCALE_EN['PRIM:GoToEdge'] = 'GoToEdge';
LOCALE_EN['PRIM:EmptyBoardContents'] = 'EmptyBoardContents';
LOCALE_EN['PRIM:numStones'] = 'numStones';
LOCALE_EN['PRIM:anyStones'] = 'anyStones';
LOCALE_EN['PRIM:canMove'] = 'canMove';
LOCALE_EN['PRIM:next'] = 'next';
LOCALE_EN['PRIM:prev'] = 'prev';
LOCALE_EN['PRIM:opposite'] = 'opposite';
LOCALE_EN['PRIM:minBool'] = 'minBool';
LOCALE_EN['PRIM:maxBool'] = 'maxBool';
LOCALE_EN['PRIM:minColor'] = 'minColor';
LOCALE_EN['PRIM:maxColor'] = 'maxColor';
LOCALE_EN['PRIM:minDir'] = 'minDir';
LOCALE_EN['PRIM:maxDir'] = 'maxDir';
LOCALE_EN['PRIM:head'] = 'head';
LOCALE_EN['PRIM:tail'] = 'tail';
LOCALE_EN['PRIM:oldTail'] = 'tail';
LOCALE_EN['PRIM:init'] = 'init';
LOCALE_EN['PRIM:last'] = 'last';

const keyword = (palabra) => `‘a palavra chave "${palabra}"`;
// Only for typing purposes
// eslint-disable-next-line @typescript-eslint/ban-types
const toFunc = (x) => x;
function pluralize(n, singular, plural) {
    if (n === 0) {
        return 'nenhum ' + singular;
    }
    else if (n === 1) {
        return 'um ' + singular;
    }
    else {
        return n.toString() + ' ' + plural;
    }
}
const LOCALE_PT = {};
for (const key in LOCALE_ES) {
    LOCALE_PT[key] = LOCALE_ES[key];
}
/* Descriptions of syntactic constructions and tokens */
LOCALE_PT['definition'] = 'uma definição (de programa, função, procedimento, ou tipo)';
LOCALE_PT['pattern'] = 'um padrão (comodín "_", construtor aplicado a variáveis, ou tupla)';
LOCALE_PT['statement'] = 'um comando';
LOCALE_PT['expression'] = 'uma expressão';
LOCALE_PT['procedure call'] = 'uma invocação a um procedimento';
LOCALE_PT['field name'] = 'o nome de um campo';
LOCALE_PT['T_EOF'] = 'o fim do arquivo';
LOCALE_PT['T_NUM'] = 'um número';
LOCALE_PT['T_STRING'] = 'uma corrente (string)';
LOCALE_PT['T_UPPERID'] = 'um identificador com maiúsculas';
LOCALE_PT['T_LOWERID'] = 'um identificador com minúsculas';
LOCALE_PT['T_PROGRAM'] = keyword('program');
LOCALE_PT['T_INTERACTIVE'] = keyword('interactive');
LOCALE_PT['T_PROCEDURE'] = keyword('procedure');
LOCALE_PT['T_FUNCTION'] = keyword('function');
LOCALE_PT['T_RETURN'] = keyword('return');
LOCALE_PT['T_IF'] = keyword('if');
LOCALE_PT['T_THEN'] = keyword('then');
LOCALE_PT['T_ELSE'] = keyword('else');
LOCALE_PT['T_REPEAT'] = keyword('repeat');
LOCALE_PT['T_FOREACH'] = keyword('foreach');
LOCALE_PT['T_IN'] = keyword('in');
LOCALE_PT['T_WHILE'] = keyword('while');
LOCALE_PT['T_SWITCH'] = keyword('switch');
LOCALE_PT['T_TO'] = keyword('to');
LOCALE_PT['T_LET'] = keyword('let');
LOCALE_PT['T_NOT'] = keyword('not');
LOCALE_PT['T_DIV'] = keyword('div');
LOCALE_PT['T_MOD'] = keyword('mod');
LOCALE_PT['T_TYPE'] = keyword('type');
LOCALE_PT['T_IS'] = keyword('is');
LOCALE_PT['T_RECORD'] = keyword('record');
LOCALE_PT['T_VARIANT'] = keyword('variant');
LOCALE_PT['T_CASE'] = keyword('case');
LOCALE_PT['T_FIELD'] = keyword('field');
LOCALE_PT['T_UNDERSCORE'] = 'um sublinhado ("_")';
LOCALE_PT['T_LPAREN'] = 'um parênteses esquerdo ("(")';
LOCALE_PT['T_RPAREN'] = 'um parênteses direito (")")';
LOCALE_PT['T_LBRACE'] = 'uma chave esquerda ("{")';
LOCALE_PT['T_RBRACE'] = 'uma chave direita ("}")';
LOCALE_PT['T_LBRACK'] = 'um colchete esquerdo ("[")';
LOCALE_PT['T_RBRACK'] = 'um colchete direito ("]")';
LOCALE_PT['T_COMMA'] = 'uma vírgula  (",")';
LOCALE_PT['T_SEMICOLON'] = 'um ponto e vírgula (";")';
LOCALE_PT['T_RANGE'] = 'um separador de intervalo ("..")';
LOCALE_PT['T_GETS'] = 'uma flecha para a esquerda ("<-")';
LOCALE_PT['T_PIPE'] = 'uma barra vertical ("|")';
LOCALE_PT['T_ARROW'] = 'uma flecha ("->")';
LOCALE_PT['T_ASSIGN'] = 'um operador de designação  (":=")';
LOCALE_PT['T_EQ'] = 'uma comparação por igualdade ("==")';
LOCALE_PT['T_NE'] = 'uma comparação por desigualdade ("/=")';
LOCALE_PT['T_LE'] = 'um menor ou igual ("<=")';
LOCALE_PT['T_GE'] = 'um maior ou igual (">=")';
LOCALE_PT['T_LT'] = 'um menor estrito ("<")';
LOCALE_PT['T_GT'] = 'um maior estrito (">")';
LOCALE_PT['T_AND'] = 'o "e" lógico ("&&")';
LOCALE_PT['T_OR'] = 'o "ou" lógico ("||")';
LOCALE_PT['T_CONCAT'] = 'o operador de concatenação de listas ("++")';
LOCALE_PT['T_PLUS'] = 'o operador de soma ("+")';
LOCALE_PT['T_MINUS'] = 'o operador de diferença ("-")';
LOCALE_PT['T_TIMES'] = 'o operador de produto ("*")';
LOCALE_PT['T_POW'] = 'o operador de potência ("^")';
/* Local name categories */
LOCALE_PT['LocalVariable'] = 'variável';
LOCALE_PT['LocalIndex'] = 'índice';
LOCALE_PT['LocalParameter'] = 'parâmetro';
/* Descriptions of value types */
LOCALE_PT['V_Integer'] = 'um número';
LOCALE_PT['V_String'] = 'uma cadeia';
LOCALE_PT['V_Tuple'] = 'uma tupla';
LOCALE_PT['V_List'] = 'uma lista';
LOCALE_PT['V_Structure'] = 'uma estrutura';
/* Lexer */
LOCALE_PT['errmsg:unclosed-multiline-comment'] = 'O comentário abre mas nunca fecha.';
LOCALE_PT['errmsg:unclosed-string-constant'] =
    'As aspas que abrem não possuem as aspas correspondentes que fecham.';
LOCALE_PT['errmsg:numeric-constant-should-not-have-leading-zeroes'] = `As constantes numéricas não podem ser escritas com zeros à esquerda.`;
LOCALE_PT['errmsg:identifier-must-start-with-alphabetic-character'] = `Os identificadores devem começar com um caractere alfabético (a...z,A...Z).`;
LOCALE_PT['errmsg:unknown-token'] = (symbol) => `Símbolo desconhecido na entrada: "${symbol}".`;
LOCALE_PT['warning:empty-pragma'] = 'Diretiva pragma vazia.';
LOCALE_PT['warning:unknown-pragma'] = (pragmaName) => 'Diretiva pragma desconhecida: "' + pragmaName + '".';
/* Parser */
LOCALE_PT['errmsg:empty-source'] = 'O programa está vazio.';
LOCALE_PT['errmsg:expected-but-found'] = (expected, found) => `Esperava-se ${expected}.
Encontrado: ${found}.`;
LOCALE_PT['errmsg:pattern-number-cannot-be-negative-zero'] = 'O padrão numérico não pode ser "-0".';
LOCALE_PT['errmsg:pattern-tuple-cannot-be-singleton'] =
    'O padrão para uma tupla não pode ter apenas um componente. ' +
        'As tuplas têm 0, 2, 3, ou mais componentes, mas não 1.';
LOCALE_PT['errmsg:assignment-tuple-cannot-be-singleton'] =
    'A designação a uma tupla não pode ser ' +
        ' constituída por apenas um componente. ' +
        'As tuplas têm 0, 2, 3, ou mais componentes, mas não 1.';
LOCALE_PT['errmsg:operators-are-not-associative'] = (op1, op2) => 'A expressão usa ' +
    op1 +
    ' e ' +
    op2 +
    ', mas estes operadores não podem ser associados. ' +
    'Talvez faltam parênteses.';
LOCALE_PT['errmsg:obsolete-tuple-assignment'] =
    'Esperava-se um comando mas não foi encontrado um parênteses esquerdo. ' +
        'Nota: a sintaxe de designação de tuplas "(x1, ..., xN) := y" ' +
        'está obsoleta. Usar "let (x1, ..., xN) := y".';
/* Linter */
LOCALE_PT['errmsg:program-already-defined'] = (pos1, pos2) => 'Já havia um programa definido em ' +
    pos1 +
    '.\n' +
    'Não é possível definir um programa em ' +
    pos2 +
    '.';
LOCALE_PT['errmsg:procedure-already-defined'] = (name, pos1, pos2) => 'O procedimiento "' +
    name +
    '" está definido duas vezes: ' +
    'em ' +
    pos1 +
    ' e em ' +
    pos2 +
    '.';
LOCALE_PT['errmsg:function-already-defined'] = (name, pos1, pos2) => `A função "${name}" está definida duas vezes: em ${pos1} e em ${pos2}.`;
LOCALE_PT['errmsg:type-already-defined'] = (name, pos1, pos2) => `O tipo "${name}" está definido duas vezes: em ${pos1} e em ${pos2}.`;
LOCALE_PT['errmsg:constructor-already-defined'] = (name, pos1, pos2) => `O construtor "${name}" está definido duas vezes: em ${pos1} e em ${pos2}.`;
LOCALE_PT['errmsg:repeated-field-name'] = (constructorName, fieldName) => 'O campo "' +
    fieldName +
    '" não pode estar repetido ' +
    'para o construtor "' +
    constructorName +
    '".';
LOCALE_PT['errmsg:function-and-field-cannot-have-the-same-name'] = (name, posFunction, posField) => 'O nome "' +
    name +
    '" usa-se ' +
    'para uma função em ' +
    posFunction +
    ' e ' +
    'para um campo em ' +
    posField +
    '.';
LOCALE_PT['errmsg:source-should-have-a-program-definition'] =
    /* Note: the code may actually be completely empty, but
     * we avoid this technicality since the message could be
     * confusing. */
    'O código deve ter uma definição de "program { ... }".';
LOCALE_PT['errmsg:procedure-should-not-have-return'] = (name) => `O procedimento "${name}" não deveria ter um comando "return".`;
LOCALE_PT['errmsg:function-should-have-return'] = (name) => 'A função "' + name + '" deveria ter um comando "return".';
LOCALE_PT['errmsg:return-statement-not-allowed-here'] =
    'O comando "return"  pode aparecer apenas como o último comando ' +
        'de uma função ou como o último comando do programa.';
LOCALE_PT['errmsg:local-name-conflict'] = (name, oldCat, oldPos, newCat, newPos) => 'Conflito de nomes: "' +
    name +
    '" se usa duas vezes: ' +
    'como ' +
    oldCat +
    ' em ' +
    oldPos +
    ', e ' +
    'como ' +
    newCat +
    ' em ' +
    newPos +
    '.';
LOCALE_PT['errmsg:repeated-variable-in-tuple-assignment'] = (name) => `La variável "${name}" está repetida na designação de tuplas.`;
LOCALE_PT['errmsg:constructor-used-as-procedure'] = (name, type) => 'O procedimento "' +
    name +
    '" não está definido. ' +
    'O nome "' +
    name +
    '" é o nome de um construtor ' +
    'do tipo "' +
    type +
    '".';
LOCALE_PT['errmsg:undefined-procedure'] = (name) => 'O procedimento "' + name + '" não está definido.';
LOCALE_PT['errmsg:undefined-function'] = (name) => 'A função "' + name + '" não está definida.';
LOCALE_PT['errmsg:procedure-arity-mismatch'] = (name, expected, received) => 'O procedimento "' +
    name +
    '" espera receber ' +
    toFunc(LOCALE_ES['<n>-parameters'])(expected) +
    ' mas é invocado com ' +
    toFunc(LOCALE_ES['<n>-arguments'])(received) +
    '.';
LOCALE_PT['errmsg:function-arity-mismatch'] = (name, expected, received) => 'A função "' +
    name +
    '" espera receber ' +
    toFunc(LOCALE_ES['<n>-parameters'])(expected) +
    ' mas é invocado com ' +
    toFunc(LOCALE_ES['<n>-arguments'])(received) +
    '.';
LOCALE_PT['errmsg:structure-pattern-arity-mismatch'] = (name, expected, received) => 'O construtor "' +
    name +
    '" tem ' +
    toFunc(LOCALE_ES['<n>-fields'])(expected) +
    ' mas o padrão tem ' +
    toFunc(LOCALE_ES['<n>-parameters'])(received) +
    '.';
LOCALE_PT['errmsg:type-used-as-constructor'] = (name, constructorNames) => {
    let msg;
    if (constructorNames.length === 0) {
        msg = '(não tem construtores).';
    }
    else if (constructorNames.length === 1) {
        msg = '(tem um construtor: ' + constructorNames[0] + ').';
    }
    else {
        msg = '(seus construtores são: ' + constructorNames.join(', ') + ').';
    }
    return ('O construtor "' +
        name +
        '" não está definido. ' +
        'O nome "' +
        name +
        '" é o nome de um tipo ' +
        msg);
};
LOCALE_PT['errmsg:procedure-used-as-constructor'] = (name) => 'O construtor "' +
    name +
    '" não está definido. ' +
    'O nome "' +
    name +
    '" é o nome de um procedimento.';
LOCALE_PT['errmsg:undeclared-constructor'] = (name) => 'O construtor "' + name + '" não está definido.';
LOCALE_PT['errmsg:wildcard-pattern-should-be-last'] =
    'O comodín "_" tem que ser o último ramo do switch.';
LOCALE_PT['errmsg:numeric-pattern-repeats-number'] = (number) => 'Tem dois ramos diferentes para o número "' + number + '".';
LOCALE_PT['errmsg:structure-pattern-repeats-constructor'] = (name) => 'Há dois ramos distintos para o construtor "' + name + '".';
LOCALE_PT['errmsg:structure-pattern-repeats-tuple-arity'] = (arity) => 'Há dois ramos distintos para as tuplas de ' + arity.toString() + ' componentes.';
LOCALE_PT['errmsg:structure-pattern-repeats-timeout'] = 'Há dois ramos distintos para o TIMEOUT.';
LOCALE_PT['errmsg:pattern-does-not-match-type'] = (expectedType, patternType) => 'Os padrões devem ser todos do mesmo tipo. ' +
    'O padrão deveria ser de tipo "' +
    expectedType +
    '" ' +
    'pero es de tipo "' +
    patternType +
    '".';
LOCALE_PT['errmsg:patterns-in-interactive-program-must-be-events'] =
    'Os padrões de um "interactive program" devem ser eventos.';
LOCALE_PT['errmsg:patterns-in-switch-must-not-be-events'] =
    'Os padrões de um "switch" não podem ser eventos.';
LOCALE_PT['errmsg:structure-construction-repeated-field'] = (constructorName, fieldName) => 'O campo "' +
    fieldName +
    '" está repetido em ' +
    'a instanciação do construtor "' +
    constructorName +
    '".';
LOCALE_PT['errmsg:structure-construction-invalid-field'] = (constructorName, fieldName) => 'O campo "' +
    fieldName +
    '" não é um campo válido ' +
    'para o construtor "' +
    constructorName +
    '".';
LOCALE_PT['errmsg:structure-construction-missing-field'] = (constructorName, fieldName) => `Falta dar valor ao campo "${fieldName}" do construtor "${constructorName}".`;
LOCALE_PT['errmsg:structure-construction-cannot-be-an-event'] = (constructorName) => 'O construtor "' +
    constructorName +
    '" corresponde a um ' +
    'evento, e só pode ser administrado implicitamente ' +
    'em um programa interativo (o usuário não pode construir ' +
    'instâncias).';
/* Runtime errors (virtual machine) */
LOCALE_PT['errmsg:undefined-variable'] = (variableName) => 'A variável "' + variableName + '" não está definida.';
LOCALE_PT['errmsg:too-few-arguments'] = (routineName) => 'Faltam argumentos para "' + routineName + '".';
LOCALE_PT['errmsg:expected-structure-but-got'] = (constructorName, valueTag) => 'Esperava-se uma estrutura construída ' +
    'com o construtor "' +
    constructorName +
    '", ' +
    'mas foi recebido ' +
    valueTag +
    '.';
LOCALE_PT['errmsg:expected-constructor-but-got'] = (constructorNameExpected, constructorNameReceived) => 'Esperava-se uma estrutura construída ' +
    'com o construtor "' +
    constructorNameExpected +
    '", ' +
    'mas o construtor recebido é ' +
    constructorNameReceived +
    '".';
LOCALE_PT['errmsg:incompatible-types-on-assignment'] = (variableName, oldType, newType) => 'A variável "' +
    variableName +
    '" ' +
    'continha un valor do tipo ' +
    oldType +
    ', ' +
    'não é possível designar um valor de tipo ' +
    newType +
    '".';
LOCALE_PT['errmsg:incompatible-types-on-list-creation'] = (index, oldType, newType) => 'Todos os elementos de uma lista devem ser do mesmo tipo. ' +
    'Os elementos são do tipo ' +
    oldType +
    ', ' +
    'mas o elemento na posição ' +
    index.toString() +
    ' ' +
    'é do tipo ' +
    newType +
    '.';
LOCALE_PT['errmsg:incompatible-types-on-structure-update'] = (fieldName, oldType, newType) => 'O campo "' +
    fieldName +
    '" é do tipo ' +
    oldType +
    '. ' +
    'Não pode ser atualizado com um valor do tipo ' +
    newType +
    '.';
LOCALE_PT['errmsg:expected-tuple-value-but-got'] = (receivedType) => `Esperava-se uma tupla mas um valor não foi recebido de tipo ${receivedType}.`;
LOCALE_PT['errmsg:tuple-component-out-of-bounds'] = (size, index) => 'Índice fora do intervalo. ' +
    'A tupla é do tamanho ' +
    size.toString() +
    ' e ' +
    'o índice é ' +
    index.toString() +
    '.';
LOCALE_PT['errmsg:expected-structure-value-but-got'] = (receivedType) => `Se esperaba una estructura pero se recibió un valor de tipo ${receivedType}.`;
LOCALE_PT['errmsg:structure-field-not-present'] = (fieldNames, missingFieldName) => 'A estrutura não possui um campo "' +
    missingFieldName +
    '". ' +
    'Os campos são: [' +
    fieldNames.join(', ') +
    '].';
LOCALE_PT['errmsg:primitive-does-not-exist'] = (primitiveName) => `A operação primitiva "${primitiveName}" não existe ou não está disponível.`;
LOCALE_PT['errmsg:primitive-arity-mismatch'] = (name, expected, received) => 'A operação "' +
    name +
    '" espera receber ' +
    toFunc(LOCALE_ES['<n>-parameters'])(expected) +
    ' mas é invocada com ' +
    toFunc(LOCALE_ES['<n>-arguments'])(received) +
    '.';
LOCALE_PT['errmsg:primitive-argument-type-mismatch'] = (name, parameterIndex, expectedType, receivedType) => 'O parâmetro #' +
    parameterIndex.toString() +
    ' ' +
    'da operação "' +
    name +
    '" ' +
    'deveria ser do tipo ' +
    expectedType +
    ' ' +
    'mas o argumento é do tipo ' +
    receivedType +
    '.';
LOCALE_PT['errmsg:expected-value-of-type-but-got'] = (expectedType, receivedType) => 'Esperava-se um valor do tipo ' +
    expectedType +
    ' ' +
    'mas foi recebido um valor do tipo ' +
    receivedType +
    '.';
LOCALE_PT['errmsg:expected-value-of-some-type-but-got'] = (expectedTypes, receivedType) => 'Esperava-se um valor de algum dos seguintes tipos: ' +
    expectedTypes.join(', ') +
    '; mas foi recebido um valor do tipo ' +
    receivedType +
    '.';
LOCALE_PT['errmsg:expected-values-to-have-compatible-types'] = (type1, type2) => 'Os tipos dos valores devem ser compatíveis, ' +
    'mas um é do tipo ' +
    type1 +
    ' ' +
    'e o outro é do tipo ' +
    type2 +
    '.';
LOCALE_PT['errmsg:switch-does-not-match'] =
    'O valor analisado não coincide com nenhum dos ramos do switch.';
LOCALE_PT['errmsg:cannot-divide-by-zero'] = 'Não é possível dividir por zero.';
LOCALE_PT['errmsg:list-cannot-be-empty'] = 'A lista não pode ser vazia.';
LOCALE_PT['errmsg:timeout'] = (millisecs) => 'A execução do programa demorou mais de ' + millisecs.toString() + 'ms.';
/* Board operations */
LOCALE_PT['errmsg:cannot-move-to'] = (dirName) => 'Não é possível mover para a direção ' + dirName + ': cai fora do tabuleiro.';
LOCALE_PT['errmsg:cannot-remove-stone'] = (dirName) => 'Não é posível retirar uma pedra de cor ' + dirName + ': não há pedras dessa cor.';
/* Runtime */
LOCALE_PT['TYPE:Color'] = 'Cor';
LOCALE_PT['CONS:Color0'] = 'Azul';
LOCALE_PT['CONS:Color1'] = 'Preto';
LOCALE_PT['CONS:Color2'] = 'Vermelho';
LOCALE_PT['CONS:Color3'] = 'Verde';
LOCALE_PT['TYPE:Dir'] = 'Dir';
LOCALE_PT['CONS:Dir0'] = 'Norte';
LOCALE_PT['CONS:Dir1'] = 'Leste';
LOCALE_PT['CONS:Dir2'] = 'Sul';
LOCALE_PT['CONS:Dir3'] = 'Oeste';
LOCALE_PT['PRIM:PutStone'] = 'Colocar';
LOCALE_PT['PRIM:RemoveStone'] = 'Retirar';
LOCALE_PT['PRIM:Move'] = 'Mover';
LOCALE_PT['PRIM:GoToEdge'] = 'IrABorda';
LOCALE_PT['PRIM:EmptyBoardContents'] = 'EsvaziarTabuleiro';
LOCALE_PT['PRIM:numStones'] = 'nroPedras';
LOCALE_PT['PRIM:anyStones'] = 'haPedras';
LOCALE_PT['PRIM:canMove'] = 'podeMover';
LOCALE_PT['PRIM:next'] = 'seguinte';
LOCALE_PT['PRIM:prev'] = 'previo';
LOCALE_PT['PRIM:opposite'] = 'oposto';
LOCALE_PT['PRIM:minBool'] = 'minBool';
LOCALE_PT['PRIM:maxBool'] = 'maxBool';
LOCALE_PT['PRIM:minColor'] = 'minCor';
LOCALE_PT['PRIM:maxColor'] = 'maxCor';
LOCALE_PT['PRIM:minDir'] = 'minDir';
LOCALE_PT['PRIM:maxDir'] = 'maxDir';
LOCALE_PT['PRIM:head'] = 'primeiro';
LOCALE_PT['PRIM:tail'] = 'resto';
LOCALE_PT['PRIM:oldTail'] = 'resto';
LOCALE_PT['PRIM:init'] = 'comeco';
LOCALE_PT['PRIM:last'] = 'ultimo';
/* Helpers */
LOCALE_PT['<alternative>'] = (strings) => 'alguma das seguintes alternativas:\n' + strings.map((s) => '  ' + s).join('\n');
LOCALE_PT['<position>'] = (filename, line, column) => filename + ':' + line.toString() + ':' + column.toString();
LOCALE_PT['<n>-parameters'] = (n) => pluralize(n, 'parâmetro', 'parâmetros');
LOCALE_PT['<n>-arguments'] = (n) => pluralize(n, 'argumento', 'argumentos');
LOCALE_PT['<n>-fields'] = (n) => pluralize(n, 'campo', 'campos');
LOCALE_PT['<pattern-type>'] = (patternType) => {
    if (patternType === 'Event') {
        return 'evento do programa interativo';
    }
    else if (patternType.substring(0, 7) === '_TUPLE_') {
        return 'tupla de ' + patternType.substring(7) + ' componentes';
    }
    else {
        return patternType;
    }
};

/* eslint-disable @typescript-eslint/ban-types */
let CURRENT_LANGUAGE = 'es';
const dictionaries = {
    es: LOCALE_ES,
    en: LOCALE_EN,
    pt: LOCALE_PT
};
const i18n = (message) => dictionaries[CURRENT_LANGUAGE][message];

/* eslint-disable no-underscore-dangle */
/* Each value has a type.
 *
 * A type is a tree, represented with instances of Type (or its subclasses).
 * We write:
 *   r(c1, ..., cN)
 * for a tree whose root is r and whose children are c1, ..., cN.
 *
 * The type of a value may be one of the following:
 *   new TypeAny()                      (unknown)
 *   new TypeInteger()
 *   new TypeString()
 *   new TypeTuple([t1, ..., tN])
 *     where ti is the type of the i-th component.
 *   new TypeList(t)
 *     where t is the type of the elements.
 *   new TypeStructure(typeName, cases)
 *     where typeName is the name of the type (e.g. 'Bool').
 *     Moreover, cases is an object of the following "type":
 *       Map String (Map String Type)
 *     more precisely,
 *     - cases is dictionary indexed by constructor names,
 *     - if c is a constructor name, cases[c] is a dictionary
 *       indexed by field name,
 *     - if f is a field name, cases[c][f] is the type of the
 *       field f for the constructor c.
 *
 *     For example, consider the following type definition:
 *       type A is variant {
 *         case B {
 *           field x
 *           field y
 *         }
 *         case C {
 *           field z
 *         }
 *       }
 *
 *    Then the following expression in Gobstones:
 *      [B(x <- 1, y <- "foo")]
 *    is a list whose type is represented as:
 *      new TypeList(
 *        new TypeStructure('A', {
 *          'B': {'x': new TypeInteger(), 'y': new TypeString()}
 *        })
 *      )
 *
 *    The following expression in Gobstones:
 *      [B(x <- 1, y <- "foo"), C(z <- "bar")]
 *    is a list whose type is represented as:
 *      new TypeList(
 *        new TypeStructure('A', {
 *          'B': {'x': new TypeInteger(), 'y': new TypeString()},
 *          'C': {'z': new TypeString()},
 *        })
 *      )
 */
const Ty_Any = Symbol.for('Ty_Any');
const Ty_Integer = Symbol.for('Ty_Integer');
const Ty_String = Symbol.for('Ty_String');
const Ty_Tuple = Symbol.for('Ty_Tuple');
const Ty_List = Symbol.for('Ty_List');
const Ty_Structure = Symbol.for('Ty_Structure');
const Ty_Unkown = Symbol.for('?');
class Type {
    constructor(tag) {
        this._tag = tag;
    }
    get tag() {
        return this._tag;
    }
    isAny() {
        return false;
    }
    isInteger() {
        return false;
    }
    isString() {
        return false;
    }
    isTuple() {
        return false;
    }
    isList() {
        return false;
    }
    isStructure() {
        return false;
    }
    isBoolean() {
        return false;
    }
    isColor() {
        return false;
    }
    isDirection() {
        return false;
    }
}
class TypeAny extends Type {
    constructor() {
        super(Ty_Any);
    }
    toString() {
        return '?';
    }
    isAny() {
        return true;
    }
}
class TypeInteger extends Type {
    constructor() {
        super(Ty_Integer);
    }
    toString() {
        return i18n('TYPE:Integer');
    }
    isInteger() {
        return true;
    }
}
class TypeString extends Type {
    constructor() {
        super(Ty_String);
    }
    toString() {
        return i18n('TYPE:String');
    }
    isString() {
        return true;
    }
}
class TypeTuple extends Type {
    constructor(componentTypes) {
        super(Ty_Tuple);
        this._componentTypes = componentTypes;
    }
    get componentTypes() {
        return this._componentTypes;
    }
    toString() {
        const strings = [];
        for (const t of this._componentTypes) {
            strings.push(t.toString());
        }
        return i18n('TYPE:Tuple') + '(' + strings.join(', ') + ')';
    }
    isTuple() {
        return true;
    }
}
class TypeList extends Type {
    constructor(contentType) {
        super(Ty_List);
        this._contentType = contentType;
    }
    get contentType() {
        return this._contentType;
    }
    toString() {
        let suffix = '';
        if (!this._contentType.isAny()) {
            suffix = '(' + this._contentType.toString() + ')';
        }
        return i18n('TYPE:List') + suffix;
    }
    isList() {
        return true;
    }
}
class TypeStructure extends Type {
    constructor(typeName, cases) {
        super(Ty_Structure);
        this._typeName = typeName;
        this._cases = cases;
    }
    get typeName() {
        return this._typeName;
    }
    get cases() {
        return this._cases;
    }
    toString() {
        const caseStrings = [];
        for (const constructorName of sortedKeys(this._cases)) {
            const fieldTypes = this._cases[constructorName];
            const fieldStrings = [];
            for (const fieldName of sortedKeys(fieldTypes)) {
                fieldStrings.push(fieldName + ' <- ' + fieldTypes[fieldName].toString());
            }
            if (fieldStrings.length !== 0) {
                caseStrings.push(constructorName + '(' + fieldStrings.join(', ') + ')');
            }
        }
        if (caseStrings.length === 0) {
            return this._typeName;
        }
        else {
            return this._typeName + ' { ' + caseStrings.join(' | ') + ' }';
        }
    }
    isStructure() {
        return true;
    }
    isBoolean() {
        return this._typeName === i18n('TYPE:Bool');
    }
    isColor() {
        return this._typeName === i18n('TYPE:Color');
    }
    isDirection() {
        return this._typeName === i18n('TYPE:Dir');
    }
}
/* Attempts to calculate the "join" of two types.
 *
 * To join two types:
 * - any occurrence of TypeAny() may be replaced by an arbitrary type,
 * - structures of the same type built with different constructors
 *   are joinable,
 * - structures of the same type built with the same constructors
 *   are joinable if their matching fields are joinable.
 *
 * If the types are joinable, return their join.
 * If the types are not joinable, return undefined.
 */
function joinTypes(type1, type2) {
    if (type1 === undefined || type2 === undefined) {
        return undefined;
    }
    else if (type1.tag === Ty_Any) {
        return type2;
    }
    else if (type2.tag === Ty_Any) {
        return type1;
    }
    else if (type1.tag === Ty_Integer && type2.tag === Ty_Integer) {
        return type1;
    }
    else if (type1.tag === Ty_String && type2.tag === Ty_String) {
        return type1;
    }
    else if (type1.tag === Ty_Tuple && type2.tag === Ty_Tuple) {
        return joinTupleTypes(type1, type2);
    }
    else if (type1.tag === Ty_List && type2.tag === Ty_List) {
        return joinListTypes(type1, type2);
    }
    else if (type1.tag === Ty_Structure && type2.tag === Ty_Structure) {
        return joinStructureTypes(type1, type2);
    }
    else {
        /* Otherwise the types are not joinable */
        return undefined;
    }
}
const joinTupleTypes = (type1, type2) => {
    if (type1.componentTypes.length !== type2.componentTypes.length) {
        /* Tuples are of different length */
        return undefined;
    }
    const joinedComponents = [];
    for (let i = 0; i < type1.componentTypes.length; i++) {
        const t1 = type1.componentTypes[i];
        const t2 = type2.componentTypes[i];
        const tj = joinTypes(t1, t2);
        if (tj === undefined) {
            /* Cannot join the i-th component */
            return undefined;
        }
        joinedComponents.push(tj);
    }
    return new TypeTuple(joinedComponents);
};
const joinListTypes = (type1, type2) => {
    const joinedContent = joinTypes(type1.contentType, type2.contentType);
    if (joinedContent === undefined) {
        /* Cannot join the contents of the lists */
        return undefined;
    }
    return new TypeList(joinedContent);
};
/*
 * The join of two structures is quite like a least common multiple.
 * We must:
 * - Check that they are structures of the same type.
 * - Include all the non-common constructors verbatim
 *   (with "non-common" we mean those that are in type1
 *   but not in type2 or vice-versa).
 * - For all common constructors, we must recursively join
 *   the types of their respective fields.
 */
const joinStructureTypes = (type1, type2) => {
    if (type1.typeName !== type2.typeName) {
        return undefined;
    }
    const joinedCases = {};
    /* Include all the non-common constructors */
    function joinCommon(typeA, typeB) {
        for (const constructorName in typeA.cases) {
            if (!(constructorName in typeB.cases)) {
                joinedCases[constructorName] = typeA.cases[constructorName];
            }
        }
    }
    joinCommon(type1, type2);
    joinCommon(type2, type1);
    /* Include all the common constructors */
    for (const constructorName in type1.cases) {
        if (constructorName in type2.cases) {
            const joinedFields = joinFields(type1.cases[constructorName], type2.cases[constructorName]);
            if (joinedFields === undefined) {
                return undefined;
            }
            joinedCases[constructorName] = joinedFields;
        }
    }
    return new TypeStructure(type1.typeName, joinedCases);
};
const joinFields = (fields1, fields2) => {
    /* Ensure that they have the same set of fields */
    function checkIncluded(fieldsA, fieldsB) {
        for (const fieldName in fieldsA) {
            if (!(fieldName in fieldsB)) {
                throw Error('Join fields: structures built using the same constructor ' +
                    'should have the same set of fields.');
            }
        }
    }
    checkIncluded(fields1, fields2);
    checkIncluded(fields2, fields1);
    /* Recursively join the types of the common fields */
    const joinedFields = {};
    for (const fieldName in fields1) {
        const type1 = fields1[fieldName];
        const type2 = fields2[fieldName];
        const joinedTypes = joinTypes(type1, type2);
        if (joinedTypes === undefined) {
            return undefined;
        }
        joinedFields[fieldName] = joinedTypes;
    }
    return joinedFields;
};
/* Helper function */
function sortedKeys(dictionary) {
    const keys = [];
    for (const key in dictionary) {
        keys.push(key);
    }
    return keys.sort();
}
/* Value tags */
const V_Integer = Symbol.for('V_Integer');
const V_String = Symbol.for('V_String');
const V_Tuple = Symbol.for('V_Tuple');
const V_List = Symbol.for('V_List');
const V_Structure = Symbol.for('V_Structure');
class Value {
    constructor(tag) {
        this._tag = tag;
    }
    get tag() {
        return this._tag;
    }
    type() {
        return new Type(Ty_Unkown);
    }
    isInteger() {
        return this.type().isInteger();
    }
    isString() {
        return this.type().isString();
    }
    isTuple() {
        return this.type().isTuple();
    }
    isList() {
        return this.type().isList();
    }
    isStructure() {
        return this.type().isStructure();
    }
    isBoolean() {
        return this.type().isBoolean();
    }
    equal(other) {
        return false;
    }
}
class ValueInteger extends Value {
    constructor(number) {
        super(V_Integer);
        this._number = typeof number === 'number' ? number : parseInt(number, 10);
    }
    toString() {
        return this._number.toString();
    }
    get number() {
        return this._number;
    }
    type() {
        return new TypeInteger();
    }
    equal(other) {
        return other.tag === V_Integer && this.number === other.number;
    }
    add(other) {
        const a = this._number;
        const b = other._number;
        return new ValueInteger(a + b);
    }
    sub(other) {
        const a = this._number;
        const b = other._number;
        return new ValueInteger(a - b);
    }
    mul(other) {
        const a = this._number;
        const b = other._number;
        return new ValueInteger(a * b === 0 ? 0 : a * b);
    }
    /* Gobstones calculates quotients using
     * modulo (i.e.truncating towards minus infinity)
     * rather than
     * remainder (i.e.truncating towards 0).
     *
     * We need to adjust the result to match the standard Gobstones
     * semantics, namely:
     *
     * if a and b have the same sign, then
     *   a div b  =  abs(a) / abs(b)
     *
     * if a and b have different signs, then
     *   a div b  =  -((abs(a) + abs(b) - 1) / abs(b))
     *
     * Here "div" denotes the official Gobstones division operator,
     * while "/" denotes the JavaScript/bigint implementation.
     */
    div(other) {
        const z = new ValueInteger(0);
        if (this.gt(z) === other.gt(z)) {
            /* Same sign */
            const a = this.abs()._number;
            const b = other.abs()._number;
            const c = Math.floor(a / b) === 0 ? 0 : Math.floor(a / b);
            return new ValueInteger(c);
        }
        else {
            /* Different sign */
            const inc = other.abs().sub(new ValueInteger(1));
            const a = this.abs().add(inc)._number;
            const b = other.abs()._number;
            const c = Math.floor(a / b) * -1 === 0 ? 0 : Math.floor(a / b) * -1;
            return new ValueInteger(c);
        }
    }
    /* Calculate the modulus from the equation a = qb + r,
     * i.e.  r = a - qb */
    mod(other) {
        const q = this.div(other);
        return this.sub(q.mul(other));
    }
    /* Assumes that 'other' is non-negative */
    pow(other) {
        const a = this._number;
        const b = other._number;
        return new ValueInteger(Math.pow(a, b));
    }
    eq(other) {
        return this.equal(other);
    }
    ne(other) {
        return !this.equal(other);
    }
    le(other) {
        const a = this._number;
        const b = other._number;
        return a <= b;
    }
    lt(other) {
        const a = this._number;
        const b = other._number;
        return a < b;
    }
    ge(other) {
        const a = this._number;
        const b = other._number;
        return a >= b;
    }
    gt(other) {
        const a = this._number;
        const b = other._number;
        return a > b;
    }
    negate() {
        const a = this._number;
        let x = a * -1;
        x = x === 0 ? 0 : x;
        return new ValueInteger(x);
    }
    abs() {
        if (this.gt(new ValueInteger(0))) {
            return this;
        }
        else {
            return this.negate();
        }
    }
    asNumber() {
        return this._number;
    }
}
class ValueString extends Value {
    constructor(string) {
        super(V_String);
        this._string = string;
    }
    toString() {
        const res = ['"'];
        // eslint-disable-next-line @typescript-eslint/prefer-for-of
        for (let i = 0; i < this._string.length; i++) {
            const chr = this._string[i];
            switch (chr) {
                case '"':
                    res.push('\\');
                    res.push('"');
                    break;
                case '\\':
                    res.push('\\');
                    res.push('\\');
                    break;
                case '\u0007':
                    res.push('\\');
                    res.push('a');
                    break;
                case '\b':
                    res.push('\\');
                    res.push('b');
                    break;
                case '\f':
                    res.push('\\');
                    res.push('f');
                    break;
                case '\n':
                    res.push('\\');
                    res.push('n');
                    break;
                case '\r':
                    res.push('\\');
                    res.push('r');
                    break;
                case '\t':
                    res.push('\\');
                    res.push('t');
                    break;
                case '\v':
                    res.push('\\');
                    res.push('v');
                    break;
                default:
                    res.push(chr);
                    break;
            }
        }
        res.push('"');
        return res.join('');
    }
    get string() {
        return this._string;
    }
    equal(other) {
        return other.tag === V_String && this.string === other.string;
    }
    type() {
        return new TypeString();
    }
}
class ValueTuple extends Value {
    constructor(components) {
        super(V_Tuple);
        this._components = components;
        this._type = this._inferType();
    }
    toString() {
        const res = [];
        for (const component of this._components) {
            res.push(component.toString());
        }
        return '(' + res.join(', ') + ')';
    }
    get components() {
        return this._components;
    }
    size() {
        return this._components.length;
    }
    equal(other) {
        if (other.tag !== V_Tuple) {
            return false;
        }
        if (this.components.length !== other.components.length) {
            return false;
        }
        for (let i = 0; i < this.components.length; i++) {
            if (!this.components[i].equal(other.components[i])) {
                return false;
            }
        }
        return true;
    }
    type() {
        return this._type;
    }
    _inferType() {
        const componentTypes = [];
        for (const component of this._components) {
            componentTypes.push(component.type());
        }
        return new TypeTuple(componentTypes);
    }
}
class ValueList extends Value {
    constructor(elements) {
        super(V_List);
        this._elements = elements;
        this._type = this._inferType();
    }
    toString() {
        const res = [];
        for (const element of this._elements) {
            res.push(element.toString());
        }
        return '[' + res.join(', ') + ']';
    }
    get elements() {
        return this._elements;
    }
    equal(other) {
        if (other.tag !== V_List) {
            return false;
        }
        if (this.elements.length !== other.elements.length) {
            return false;
        }
        for (let i = 0; i < this.elements.length; i++) {
            if (!this.elements[i].equal(other.elements[i])) {
                return false;
            }
        }
        return true;
    }
    type() {
        return this._type;
    }
    length() {
        return this._elements.length;
    }
    _inferType() {
        let contentType = new TypeAny();
        for (const element of this._elements) {
            contentType = joinTypes(contentType, element.type());
        }
        return new TypeList(contentType);
    }
    append(other) {
        const allElements = [];
        for (const elem of this.elements) {
            allElements.push(elem);
        }
        for (const elem of other.elements) {
            allElements.push(elem);
        }
        return new ValueList(allElements);
    }
    head() {
        return this.elements[0];
    }
    tail() {
        const elements = [];
        for (let i = 1; i < this.elements.length; i++) {
            elements.push(this.elements[i]);
        }
        return new ValueList(elements);
    }
    init() {
        const elements = [];
        for (let i = 0; i < this.elements.length - 1; i++) {
            elements.push(this.elements[i]);
        }
        return new ValueList(elements);
    }
    last() {
        return this.elements[this.elements.length - 1];
    }
}
/* An instance of ValueStructure represents a 'structure' i.e.  a value
 * inhabiting an 'inductive' datatype.
 *
 * This includes built-in enumerations (e.g. booleans), the "event" type
 * received by an interactive program, and user-defined records and variants.
 *
 * The second parameter "fields" should be a dictionary mapping field names to
 * values
 */
class ValueStructure extends Value {
    constructor(typeName, constructorName, fields) {
        super(V_Structure);
        this._typeName = typeName;
        this._constructorName = constructorName;
        this._fields = fields;
    }
    toString() {
        const res = [];
        const fieldNames = this.fieldNames();
        if (fieldNames.length === 0) {
            return this._constructorName;
        }
        for (const fieldName of fieldNames) {
            res.push(fieldName + ' <- ' + this.fields[fieldName].toString());
        }
        return this._constructorName + '(' + res.join(', ') + ')';
    }
    get typeName() {
        return this._typeName;
    }
    get constructorName() {
        return this._constructorName;
    }
    get fields() {
        return this._fields;
    }
    fieldNames() {
        return sortedKeys(this._fields);
    }
    _clone() {
        const newFields = {};
        for (const fieldName in this._fields) {
            newFields[fieldName] = this._fields[fieldName];
        }
        return new ValueStructure(this._typeName, this._constructorName, newFields);
    }
    updateFields(fields) {
        const newStructure = this._clone();
        for (const fieldName in fields) {
            newStructure.fields[fieldName] = fields[fieldName];
        }
        return newStructure;
    }
    equal(other) {
        if (other.tag !== V_Structure) {
            return false;
        }
        if (this.constructorName !== other.constructorName) {
            return false;
        }
        const fieldNames = this.fieldNames();
        for (const fieldName of fieldNames) {
            if (!this.fields[fieldName].equal(other.fields[fieldName])) {
                return false;
            }
        }
        return true;
    }
    type() {
        const fieldTypes = {};
        for (const fieldName in this._fields) {
            fieldTypes[fieldName] = this._fields[fieldName].type();
        }
        const cases = {};
        cases[this._constructorName] = fieldTypes;
        return new TypeStructure(this._typeName, cases);
    }
}

/* eslint-disable no-underscore-dangle */
/*
 * This module provides the runtime support for the execution of a program.
 *
 * The runtime support includes:
 *
 * - A definition of a class RuntimeState, representing the global state
 *   of a program.
 *
 * - A definition of a class RuntimePrimitives, representing the available
 *   primitive functions.
 *
 * This file is a particular implementation, in which RuntimeState
 * represents a Gobstones board, and RuntimePrimitives are the primitives
 * functions and procedures available in Gobstones.
 *
 * Potential variants of the language might have a different notion of
 * global state, and different available primitives.
 */
function fail$1(startPos, endPos, reason, args) {
    throw new GbsRuntimeError(startPos, endPos, reason, args);
}
const boolEnum = () => [i18n('CONS:False'), i18n('CONS:True')];
const colorEnum = () => [
    i18n('CONS:Color0'),
    i18n('CONS:Color1'),
    i18n('CONS:Color2'),
    i18n('CONS:Color3')
];
const dirEnum = () => [
    i18n('CONS:Dir0'),
    i18n('CONS:Dir1'),
    i18n('CONS:Dir2'),
    i18n('CONS:Dir3')
];
/* Enumeration of all the constructors of the Event type, including
 * INIT and TIMEOUT. */
function keyEventEnum() {
    const modifiers = [
        '',
        'CTRL_',
        'ALT_',
        'SHIFT_',
        'CTRL_ALT_',
        'CTRL_SHIFT_',
        'ALT_SHIFT_',
        'CTRL_ALT_SHIFT_'
    ];
    const charKeys = [
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z',
        '0',
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9'
    ];
    const specialKeys = [
        'SPACE',
        'RETURN',
        'TAB',
        'BACKSPACE',
        'ESCAPE',
        'INSERT',
        'DELETE',
        'HOME',
        'END',
        'PAGEUP',
        'PAGEDOWN',
        'F1',
        'F2',
        'F3',
        'F4',
        'F5',
        'F6',
        'F7',
        'F8',
        'F9',
        'F10',
        'F11',
        'F12'
    ];
    const symbolKeys = [
        'AMPERSAND',
        'ASTERISK',
        'AT',
        'BACKSLASH',
        'CARET',
        'COLON',
        'DOLLAR',
        'EQUALS',
        'EXCLAIM',
        'GREATER',
        'HASH',
        'LESS',
        'PERCENT',
        'PLUS',
        'SEMICOLON',
        'SLASH',
        'QUESTION',
        'QUOTE',
        'QUOTEDBL',
        'UNDERSCORE',
        'LEFTPAREN',
        'RIGHTPAREN',
        'LEFTBRACKET',
        'RIGHTBRACKET',
        'LEFTBRACE',
        'RIGHTBRACE'
    ];
    const arrowKeys = ['LEFT', 'RIGHT', 'UP', 'DOWN'];
    const keys = charKeys.concat(specialKeys).concat(symbolKeys).concat(arrowKeys);
    const eventNames = [];
    for (const modifier of modifiers) {
        for (const key of keys) {
            eventNames.push('K_' + modifier + key);
        }
    }
    return eventNames;
}
const KEY_EVENT_ENUM = keyEventEnum();
const eventEnum = () => [i18n('CONS:INIT'), i18n('CONS:TIMEOUT')].concat(KEY_EVENT_ENUM);
const toEnum = (enumeration, name) => enumeration.indexOf(name);
const fromEnum = (enumeration, index) => enumeration[index];
const dirOpposite = (dirName) => fromEnum(dirEnum(), (toEnum(dirEnum(), dirName) + 2) % 4);
const dirNext = (dirName) => fromEnum(dirEnum(), (toEnum(dirEnum(), dirName) + 1) % 4);
const dirPrev = (dirName) => fromEnum(dirEnum(), (toEnum(dirEnum(), dirName) + 3) % 4);
const colorNext = (colorName) => fromEnum(colorEnum(), (toEnum(colorEnum(), colorName) + 1) % 4);
const colorPrev = (colorName) => fromEnum(colorEnum(), (toEnum(colorEnum(), colorName) + 3) % 4);
/*
 * An instance of RuntimeState represents the current global state of
 * a program. In the case of Gobstones, it is a Gobstones board.
 *
 * It MUST implement the following methods:
 *
 *   this.clone() ~~> returns a copy of the state
 *
 */
class RuntimeState {
    constructor() {
        /*
         * The board is represented as a list of columns, so that board[x] is the
         * x-th column and board[x][y] is the cell at (x, y).
         *
         * By default, create an empty 9x9 board.
         */
        this._width = 11;
        this._height = 7;
        this._board = [];
        for (let x = 0; x < this._width; x++) {
            const column = [];
            for (let y = 0; y < this._height; y++) {
                column.push(this._emptyCell());
            }
            this._board.push(column);
        }
        this._head = { x: 0, y: 0 };
    }
    clone() {
        const newState = new RuntimeState();
        newState._width = this._width;
        newState._height = this._height;
        newState._board = [];
        for (let x = 0; x < this._width; x++) {
            const column = [];
            for (let y = 0; y < this._height; y++) {
                const cell = {};
                for (const colorName of colorEnum()) {
                    cell[colorName] = this._board[x][y][colorName];
                }
                column.push(cell);
            }
            newState._board.push(column);
        }
        newState._head = { x: this._head.x, y: this._head.y };
        return newState;
    }
    /* Dump the state to a Jboard data structure */
    dump() {
        const jboard = {
            head: [],
            width: 0,
            height: 0,
            board: []
        };
        jboard.width = this._width;
        jboard.height = this._height;
        jboard.head = [this._head.x, this._head.y];
        jboard.board = [];
        for (let x = 0; x < this._width; x++) {
            const column = [];
            for (let y = 0; y < this._height; y++) {
                const cell = {};
                cell['a'] = this._board[x][y][i18n('CONS:Color0')].asNumber();
                cell['n'] = this._board[x][y][i18n('CONS:Color1')].asNumber();
                cell['r'] = this._board[x][y][i18n('CONS:Color2')].asNumber();
                cell['v'] = this._board[x][y][i18n('CONS:Color3')].asNumber();
                column.push(cell);
            }
            jboard.board.push(column);
        }
        return jboard;
    }
    /* Load the state from a Jboard data structure */
    load(jboard) {
        this._width = jboard.width;
        this._height = jboard.height;
        this._head.x = jboard.head[0];
        this._head.y = jboard.head[1];
        this._board = [];
        for (let x = 0; x < this._width; x++) {
            const row = [];
            for (let y = 0; y < this._height; y++) {
                const cell = jboard.board[x][y];
                const newCell = {};
                newCell[i18n('CONS:Color0')] = new ValueInteger(cell['a']);
                newCell[i18n('CONS:Color1')] = new ValueInteger(cell['n']);
                newCell[i18n('CONS:Color2')] = new ValueInteger(cell['r']);
                newCell[i18n('CONS:Color3')] = new ValueInteger(cell['v']);
                row.push(newCell);
            }
            this._board.push(row);
        }
    }
    /* Gobstones specific methods */
    putStone(colorName) {
        let n = this._board[this._head.x][this._head.y][colorName];
        n = n.add(new ValueInteger(1));
        this._board[this._head.x][this._head.y][colorName] = n;
    }
    removeStone(colorName) {
        let n = this._board[this._head.x][this._head.y][colorName];
        if (n.le(new ValueInteger(0))) {
            throw Error('Cannot remove stone.');
        }
        n = n.sub(new ValueInteger(1));
        this._board[this._head.x][this._head.y][colorName] = n;
    }
    numStones(colorName) {
        return this._board[this._head.x][this._head.y][colorName];
    }
    move(dirName) {
        if (!this.canMove(dirName)) {
            throw Error('Cannot move.');
        }
        const delta = this._deltaForDirection(dirName);
        this._head.x += delta[0];
        this._head.y += delta[1];
    }
    goToEdge(dirName) {
        if (dirName === i18n('CONS:Dir0')) {
            this._head.y = this._height - 1;
        }
        else if (dirName === i18n('CONS:Dir1')) {
            this._head.x = this._width - 1;
        }
        else if (dirName === i18n('CONS:Dir2')) {
            this._head.y = 0;
        }
        else if (dirName === i18n('CONS:Dir3')) {
            this._head.x = 0;
        }
        else {
            throw Error('Invalid direction: ' + dirName);
        }
    }
    emptyBoardContents() {
        for (let x = 0; x < this._width; x++) {
            for (let y = 0; y < this._height; y++) {
                this._board[x][y] = this._emptyCell();
            }
        }
    }
    canMove(dirName) {
        const delta = this._deltaForDirection(dirName);
        const x = this._head.x + delta[0];
        const y = this._head.y + delta[1];
        return x >= 0 && x < this._width && y >= 0 && y < this._height;
    }
    _deltaForDirection(dirName) {
        let delta;
        if (dirName === i18n('CONS:Dir0')) {
            delta = [0, 1];
        }
        else if (dirName === i18n('CONS:Dir1')) {
            delta = [1, 0];
        }
        else if (dirName === i18n('CONS:Dir2')) {
            delta = [0, -1];
        }
        else if (dirName === i18n('CONS:Dir3')) {
            delta = [-1, 0];
        }
        else {
            throw Error('Invalid direction: ' + dirName);
        }
        return delta;
    }
    _emptyCell() {
        const cell = {};
        for (const colorName of colorEnum()) {
            cell[colorName] = new ValueInteger(0);
        }
        return cell;
    }
}
class PrimitiveOperation {
    constructor(argumentTypes, argumentValidator, implementation) {
        this._argumentTypes = argumentTypes;
        this._argumentValidator = argumentValidator;
        this._implementation = implementation;
    }
    get argumentTypes() {
        return this._argumentTypes;
    }
    nargs() {
        return this._argumentTypes.length;
    }
    call(globalState, args) {
        return this._implementation.apply(undefined, [globalState].concat(args));
    }
    /* Check that the arguments are valid according to the validator.
     * The validator should be a function receiving a start and end
     * positions, and a list of arguments.
     * It should throw a GbsRuntimeError if the arguments are invalid.
     */
    validateArguments(startPos, endPos, globalState, args) {
        this._argumentValidator(startPos, endPos, globalState, args);
    }
}
/* Casting Gobstones values to JavaScript values and vice-versa */
const typeAny = new TypeAny();
const typeInteger = new TypeInteger();
const typeString = new TypeString();
const typeBool = () => new TypeStructure(i18n('TYPE:Bool'), {});
const typeListAny = new TypeList(new TypeAny());
function valueFromBool(bool) {
    if (bool) {
        return new ValueStructure(i18n('TYPE:Bool'), i18n('CONS:True'), {});
    }
    else {
        return new ValueStructure(i18n('TYPE:Bool'), i18n('CONS:False'), {});
    }
}
const boolFromValue = (value) => value.constructorName === i18n('CONS:True');
const typeColor = () => new TypeStructure(i18n('TYPE:Color'), {});
const valueFromColor = (colorName) => new ValueStructure(i18n('TYPE:Color'), colorName, {});
const colorFromValue = (value) => value.constructorName;
const typeDir = () => new TypeStructure(i18n('TYPE:Dir'), {});
const valueFromDir = (dirName) => new ValueStructure(i18n('TYPE:Dir'), dirName, {});
const dirFromValue = (value) => value.constructorName;
/* Argument validators */
function noValidation() {
    /* No validation */
}
const isInteger = (x) => joinTypes(x.type(), typeInteger) !== undefined;
const isBool = (x) => joinTypes(x.type(), typeBool()) !== undefined;
const isColor = (x) => joinTypes(x.type(), typeColor()) !== undefined;
const isDir = (x) => joinTypes(x.type(), typeDir()) !== undefined;
const typesWithOpposite = () => [typeInteger, typeBool(), typeDir()];
const typesWithOrder = () => [typeInteger, typeBool(), typeColor(), typeDir()];
/* Generic operations */
function enumIndex(value) {
    if (isBool(value)) {
        if (boolFromValue(value)) {
            return 1;
        }
        else {
            return 0;
        }
    }
    else if (isColor(value)) {
        return toEnum(colorEnum(), colorFromValue(value));
    }
    else if (isDir(value)) {
        return toEnum(dirEnum(), dirFromValue(value));
    }
    else {
        throw Error('Value should be Bool, Color or Dir.');
    }
}
function genericLE(a, b) {
    if (isInteger(a)) {
        return valueFromBool(a.le(b));
    }
    else {
        const indexA = enumIndex(a);
        const indexB = enumIndex(b);
        return valueFromBool(indexA <= indexB);
    }
}
function genericGE(a, b) {
    if (isInteger(a)) {
        return valueFromBool(a.ge(b));
    }
    else {
        const indexA = enumIndex(a);
        const indexB = enumIndex(b);
        return valueFromBool(indexA >= indexB);
    }
}
function genericLT(a, b) {
    if (isInteger(a)) {
        return valueFromBool(a.lt(b));
    }
    else {
        const indexA = enumIndex(a);
        const indexB = enumIndex(b);
        return valueFromBool(indexA < indexB);
    }
}
function genericGT(a, b) {
    if (isInteger(a)) {
        return valueFromBool(a.gt(b));
    }
    else {
        const indexA = enumIndex(a);
        const indexB = enumIndex(b);
        return valueFromBool(indexA > indexB);
    }
}
function genericNext(a) {
    if (isInteger(a)) {
        return a.add(new ValueInteger(1));
    }
    else if (isBool(a)) {
        if (boolFromValue(a)) {
            return valueFromBool(false);
        }
        else {
            return valueFromBool(true);
        }
    }
    else if (isColor(a)) {
        return valueFromColor(colorNext(colorFromValue(a)));
    }
    else if (isDir(a)) {
        return valueFromDir(dirNext(dirFromValue(a)));
    }
    else {
        throw Error('genericNext: value has no next.');
    }
}
function genericPrev(a) {
    if (isInteger(a)) {
        return a.sub(new ValueInteger(1));
    }
    else if (isBool(a)) {
        if (boolFromValue(a)) {
            return valueFromBool(false);
        }
        else {
            return valueFromBool(true);
        }
    }
    else if (isColor(a)) {
        return valueFromColor(colorPrev(colorFromValue(a)));
    }
    else if (isDir(a)) {
        return valueFromDir(dirPrev(dirFromValue(a)));
    }
    else {
        throw Error('genericPrev: value has no prev.');
    }
}
function genericOpposite(a) {
    if (isInteger(a)) {
        return a.negate();
    }
    else if (isBool(a)) {
        return valueFromBool(!boolFromValue(a));
    }
    else if (isDir(a)) {
        return valueFromDir(dirOpposite(dirFromValue(a)));
    }
    else {
        throw Error('genericOpposite: value has no opposite.');
    }
}
/* Validate that the type of 'x' is among the given list of types */
function validateTypeAmong(startPos, endPos, x, types) {
    /* Succeed if the type of x is in the list 'types' */
    for (const type of types) {
        if (joinTypes(x.type(), type) !== undefined) {
            return;
        }
    }
    /* Report error */
    fail$1(startPos, endPos, 'expected-value-of-some-type-but-got', [types, x.type()]);
}
/* Validate that the types of 'x' and 'y' are compatible */
function validateCompatibleTypes(startPos, endPos, x, y) {
    if (joinTypes(x.type(), y.type()) === undefined) {
        fail$1(startPos, endPos, 'expected-values-to-have-compatible-types', [x.type(), y.type()]);
    }
}
/* Runtime primitives */
class RuntimePrimitives {
    constructor() {
        /* this._primitiveTypes is a dictionary indexed by type names.
         *
         * this._primitiveTypes[typeName] is a dictionary indexed by
         * the constructor names of the given type.
         *
         * this._primitiveTypes[typeName][constructorName]
         * is a list of field names.
         */
        this._primitiveTypes = {};
        /* this._primitiveProcedures and this._primitiveFunctions
         * are dictionaries indexed by the name of the primitive operation
         * (procedure or function). Their value is an instance of
         * PrimitiveOperation.
         */
        this._primitiveProcedures = {};
        this._primitiveFunctions = {};
        /* --Primitive types-- */
        /* Booleans */
        this._primitiveTypes[i18n('TYPE:Bool')] = {};
        for (const boolName of boolEnum()) {
            this._primitiveTypes[i18n('TYPE:Bool')][boolName] = [];
        }
        /* Colors */
        this._primitiveTypes[i18n('TYPE:Color')] = {};
        for (const colorName of colorEnum()) {
            this._primitiveTypes[i18n('TYPE:Color')][colorName] = [];
        }
        /* Directions */
        this._primitiveTypes[i18n('TYPE:Dir')] = {};
        for (const dirName of dirEnum()) {
            this._primitiveTypes[i18n('TYPE:Dir')][dirName] = [];
        }
        /* Events */
        this._primitiveTypes[i18n('TYPE:Event')] = {};
        for (const eventName of eventEnum()) {
            this._primitiveTypes[i18n('TYPE:Event')][eventName] = [];
        }
        /* --Primitive procedures-- */
        this._primitiveProcedures[i18n('PRIM:TypeCheck')] = new PrimitiveOperation([typeAny, typeAny, typeString], (startPos, endPos, globalState, args) => {
            const v1 = args[0];
            const v2 = args[1];
            const errorMessage = args[2];
            if (joinTypes(v1.type(), v2.type()) === undefined) {
                fail$1(startPos, endPos, 'typecheck-failed', [
                    errorMessage.string,
                    v1.type(),
                    v2.type()
                ]);
            }
        }, (globalState, color) => undefined);
        this._primitiveProcedures[i18n('PRIM:PutStone')] = new PrimitiveOperation([typeColor()], noValidation, (globalState, color) => {
            globalState.putStone(colorFromValue(color));
            return undefined;
        });
        this._primitiveProcedures[i18n('PRIM:RemoveStone')] = new PrimitiveOperation([typeColor()], (startPos, endPos, globalState, args) => {
            const colorName = colorFromValue(args[0]);
            if (globalState.numStones(colorName).le(new ValueInteger(0))) {
                fail$1(startPos, endPos, 'cannot-remove-stone', [colorName]);
            }
        }, (globalState, color) => {
            globalState.removeStone(colorFromValue(color));
            return undefined;
        });
        this._primitiveProcedures[i18n('PRIM:Move')] = new PrimitiveOperation([typeDir()], (startPos, endPos, globalState, args) => {
            const dirName = dirFromValue(args[0]);
            if (!globalState.canMove(dirName)) {
                fail$1(startPos, endPos, 'cannot-move-to', [dirName]);
            }
        }, (globalState, dir) => {
            globalState.move(dirFromValue(dir));
            return undefined;
        });
        this._primitiveProcedures[i18n('PRIM:GoToEdge')] = new PrimitiveOperation([typeDir()], noValidation, (globalState, dir) => {
            globalState.goToEdge(dirFromValue(dir));
            return undefined;
        });
        this._primitiveProcedures[i18n('PRIM:EmptyBoardContents')] = new PrimitiveOperation([], noValidation, (globalState, dir) => {
            globalState.emptyBoardContents();
            return undefined;
        });
        this._primitiveProcedures['_FAIL'] =
            /* Procedure that always fails */
            new PrimitiveOperation([typeString], (startPos, endPos, globalState, args) => {
                fail$1(startPos, endPos, args[0].string, []);
            }, (globalState, errMsg /* Unreachable */) => undefined);
        /* --Primitive functions-- */
        this._primitiveFunctions['_makeRange'] = new PrimitiveOperation([typeAny, typeAny], (startPos, endPos, globalState, args) => {
            const first = args[0];
            const last = args[1];
            validateCompatibleTypes(startPos, endPos, first, last);
            validateTypeAmong(startPos, endPos, first, typesWithOrder());
            validateTypeAmong(startPos, endPos, last, typesWithOrder());
        }, (globalState, first, last) => {
            let current = first;
            if (boolFromValue(genericGT(current, last))) {
                return new ValueList([]);
            }
            const result = [];
            while (boolFromValue(genericLT(current, last))) {
                result.push(current);
                current = genericNext(current);
            }
            result.push(current);
            return new ValueList(result);
        });
        this._primitiveFunctions['not'] = new PrimitiveOperation([typeBool()], noValidation, (globalState, x) => valueFromBool(!boolFromValue(x)));
        this._primitiveFunctions['&&'] = new PrimitiveOperation([typeAny, typeAny], noValidation, 
        /*
         * This function is a stub so the linter recognizes '&&'
         * as a defined primitive function of arity 2.
         *
         * The implementation of '&&' is treated specially by the
         * compiler to account for short-circuiting.
         */
        (globalState, x, y) => {
            throw Error('The function "&&" should never be called');
        });
        this._primitiveFunctions['||'] = new PrimitiveOperation([typeAny, typeAny], noValidation, 
        /*
         * This function is a stub so the linter recognizes '||'
         * as a defined primitive function of arity 2.
         *
         * The implementation of '||' is treated specially by the
         * compiler to account for short-circuiting.
         */
        (globalState, x, y) => {
            throw Error('The function "||" should never be called');
        });
        this._primitiveFunctions['_makeRangeWithSecond'] = new PrimitiveOperation([typeAny, typeAny, typeAny], (startPos, endPos, globalState, args) => {
            const first = args[0];
            const last = args[1];
            const second = args[2];
            validateTypeAmong(startPos, endPos, first, [typeInteger]);
            validateTypeAmong(startPos, endPos, last, [typeInteger]);
            validateTypeAmong(startPos, endPos, second, [typeInteger]);
        }, (globalState, first, last, second) => {
            const delta = second.sub(first);
            if (delta.lt(new ValueInteger(1))) {
                return new ValueList([]);
            }
            let current = first;
            const result = [];
            while (current.le(last)) {
                result.push(current);
                current = current.add(delta);
            }
            return new ValueList(result);
        });
        this._primitiveFunctions['_unsafeListLength'] = new PrimitiveOperation([typeAny], noValidation, (globalState, list) => new ValueInteger(list.length()));
        this._primitiveFunctions['_unsafeListNth'] = new PrimitiveOperation([typeAny, typeAny], noValidation, (globalState, list, index) => list.elements[index.asNumber()]);
        this._primitiveFunctions[i18n('PRIM:numStones')] = new PrimitiveOperation([typeColor()], noValidation, (globalState, color) => globalState.numStones(colorFromValue(color)));
        this._primitiveFunctions[i18n('PRIM:anyStones')] = new PrimitiveOperation([typeColor()], noValidation, (globalState, color) => {
            const num = globalState.numStones(colorFromValue(color));
            return valueFromBool(num.gt(new ValueInteger(0)));
        });
        this._primitiveFunctions[i18n('PRIM:canMove')] = new PrimitiveOperation([typeDir()], noValidation, (globalState, dir) => valueFromBool(globalState.canMove(dirFromValue(dir))));
        this._primitiveFunctions[i18n('PRIM:next')] = new PrimitiveOperation([typeAny], (startPos, endPos, globalState, args) => {
            const value = args[0];
            validateTypeAmong(startPos, endPos, value, typesWithOrder());
        }, (globalState, value) => genericNext(value));
        this._primitiveFunctions[i18n('PRIM:prev')] = new PrimitiveOperation([typeAny], (startPos, endPos, globalState, args) => {
            const value = args[0];
            validateTypeAmong(startPos, endPos, value, typesWithOrder());
        }, (globalState, value) => genericPrev(value));
        this._primitiveFunctions[i18n('PRIM:opposite')] = new PrimitiveOperation([typeAny], (startPos, endPos, globalState, args) => {
            const value = args[0];
            validateTypeAmong(startPos, endPos, value, typesWithOpposite());
        }, (globalState, value) => genericOpposite(value));
        this._primitiveFunctions[i18n('PRIM:minBool')] = new PrimitiveOperation([], noValidation, (globalState) => valueFromBool(false));
        this._primitiveFunctions[i18n('PRIM:maxBool')] = new PrimitiveOperation([], noValidation, (globalState) => valueFromBool(true));
        this._primitiveFunctions[i18n('PRIM:minColor')] = new PrimitiveOperation([], noValidation, (globalState) => valueFromColor(colorEnum()[0]));
        this._primitiveFunctions[i18n('PRIM:maxColor')] = new PrimitiveOperation([], noValidation, (globalState) => valueFromColor(colorEnum()[colorEnum().length - 1]));
        this._primitiveFunctions[i18n('PRIM:minDir')] = new PrimitiveOperation([], noValidation, (globalState) => valueFromDir(dirEnum()[0]));
        this._primitiveFunctions[i18n('PRIM:maxDir')] = new PrimitiveOperation([], noValidation, (globalState) => valueFromDir(dirEnum()[dirEnum().length - 1]));
        /* Arithmetic operators */
        this._primitiveFunctions['+'] = new PrimitiveOperation([typeInteger, typeInteger], noValidation, (globalState, a, b) => a.add(b));
        this._primitiveFunctions['-'] = new PrimitiveOperation([typeInteger, typeInteger], noValidation, (globalState, a, b) => a.sub(b));
        this._primitiveFunctions['*'] = new PrimitiveOperation([typeInteger, typeInteger], noValidation, (globalState, a, b) => a.mul(b));
        this._primitiveFunctions['div'] = new PrimitiveOperation([typeInteger, typeInteger], (startPos, endPos, globalState, args) => {
            const b = args[1];
            if (b.eq(new ValueInteger(0))) {
                fail$1(startPos, endPos, 'cannot-divide-by-zero', []);
            }
        }, (globalState, a, b) => a.div(b));
        this._primitiveFunctions['mod'] = new PrimitiveOperation([typeInteger, typeInteger], (startPos, endPos, globalState, args) => {
            const b = args[1];
            if (b.eq(new ValueInteger(0))) {
                fail$1(startPos, endPos, 'cannot-divide-by-zero', []);
            }
        }, (globalState, a, b) => a.mod(b));
        this._primitiveFunctions['^'] = new PrimitiveOperation([typeInteger, typeInteger], (startPos, endPos, globalState, args) => {
            const b = args[1];
            if (b.lt(new ValueInteger(0))) {
                fail$1(startPos, endPos, 'negative-exponent', []);
            }
        }, (globalState, a, b) => a.pow(b));
        this._primitiveFunctions['-(unary)'] = new PrimitiveOperation([typeAny], (startPos, endPos, globalState, args) => {
            const a = args[0];
            validateTypeAmong(startPos, endPos, a, typesWithOpposite());
        }, (globalState, a) => genericOpposite(a));
        /* Relational operators */
        this._primitiveFunctions['=='] = new PrimitiveOperation([typeAny, typeAny], (startPos, endPos, globalState, args) => {
            const a = args[0];
            const b = args[1];
            validateCompatibleTypes(startPos, endPos, a, b);
        }, (globalState, a, b) => valueFromBool(a.equal(b)));
        this._primitiveFunctions['/='] = new PrimitiveOperation([typeAny, typeAny], (startPos, endPos, globalState, args) => {
            const a = args[0];
            const b = args[1];
            validateCompatibleTypes(startPos, endPos, a, b);
        }, (globalState, a, b) => valueFromBool(!a.equal(b)));
        this._primitiveFunctions['<='] = new PrimitiveOperation([typeAny, typeAny], (startPos, endPos, globalState, args) => {
            const a = args[0];
            const b = args[1];
            validateCompatibleTypes(startPos, endPos, a, b);
            validateTypeAmong(startPos, endPos, a, typesWithOrder());
            validateTypeAmong(startPos, endPos, b, typesWithOrder());
        }, (globalState, a, b) => genericLE(a, b));
        this._primitiveFunctions['>='] = new PrimitiveOperation([typeAny, typeAny], (startPos, endPos, globalState, args) => {
            const a = args[0];
            const b = args[1];
            validateCompatibleTypes(startPos, endPos, a, b);
            validateTypeAmong(startPos, endPos, a, typesWithOrder());
            validateTypeAmong(startPos, endPos, b, typesWithOrder());
        }, (globalState, a, b) => genericGE(a, b));
        this._primitiveFunctions['<'] = new PrimitiveOperation([typeAny, typeAny], (startPos, endPos, globalState, args) => {
            const a = args[0];
            const b = args[1];
            validateCompatibleTypes(startPos, endPos, a, b);
            validateTypeAmong(startPos, endPos, a, typesWithOrder());
            validateTypeAmong(startPos, endPos, b, typesWithOrder());
        }, (globalState, a, b) => genericLT(a, b));
        this._primitiveFunctions['>'] = new PrimitiveOperation([typeAny, typeAny], (startPos, endPos, globalState, args) => {
            const a = args[0];
            const b = args[1];
            validateCompatibleTypes(startPos, endPos, a, b);
            validateTypeAmong(startPos, endPos, a, typesWithOrder());
            validateTypeAmong(startPos, endPos, b, typesWithOrder());
        }, (globalState, a, b) => genericGT(a, b));
        /* User-triggered failure */
        this._primitiveProcedures[i18n('PRIM:BOOM')] = new PrimitiveOperation([typeString], (startPos, endPos, globalState, args) => {
            fail$1(startPos, endPos, 'boom-called', [args[0].string]);
        }, (globalState, msg) => {
            throw Error('Should not be reachable.');
        });
        this._primitiveFunctions[i18n('PRIM:boom')] = this._primitiveProcedures[i18n('PRIM:BOOM')];
        /* List operators */
        this._primitiveFunctions['++'] = new PrimitiveOperation([typeListAny, typeListAny], (startPos, endPos, globalState, args) => {
            const a = args[0];
            const b = args[1];
            validateCompatibleTypes(startPos, endPos, a, b);
        }, (globalState, a, b) => a.append(b));
        this._primitiveFunctions[i18n('PRIM:isEmpty')] = new PrimitiveOperation([typeListAny], noValidation, (globalState, a) => valueFromBool(a.length() === 0));
        this._primitiveFunctions[i18n('PRIM:head')] = new PrimitiveOperation([typeListAny], (startPos, endPos, globalState, args) => {
            const a = args[0];
            if (a.length() === 0) {
                fail$1(startPos, endPos, 'list-cannot-be-empty', []);
            }
        }, (globalState, a) => a.head());
        this._primitiveFunctions[i18n('PRIM:tail')] = new PrimitiveOperation([typeListAny], (startPos, endPos, globalState, args) => {
            const a = args[0];
            if (a.length() === 0) {
                fail$1(startPos, endPos, 'list-cannot-be-empty', []);
            }
        }, (globalState, a) => a.tail());
        this._primitiveFunctions[i18n('PRIM:oldTail')] = this._primitiveFunctions[i18n('PRIM:tail')];
        this._primitiveFunctions[i18n('PRIM:init')] = new PrimitiveOperation([typeListAny], (startPos, endPos, globalState, args) => {
            const a = args[0];
            if (a.length() === 0) {
                fail$1(startPos, endPos, 'list-cannot-be-empty', []);
            }
        }, (globalState, a) => a.init());
        this._primitiveFunctions[i18n('PRIM:last')] = new PrimitiveOperation([typeListAny], (startPos, endPos, globalState, args) => {
            const a = args[0];
            if (a.length() === 0) {
                fail$1(startPos, endPos, 'list-cannot-be-empty', []);
            }
        }, (globalState, a) => a.last());
    }
    /* Types */
    types() {
        const typeNames = [];
        for (const typeName in this._primitiveTypes) {
            typeNames.push(typeName);
        }
        return typeNames;
    }
    typeConstructors(typeName) {
        if (!(typeName in this._primitiveTypes)) {
            throw Error('Not a primitive type: ' + typeName);
        }
        const constructorNames = [];
        for (const constructorName in this._primitiveTypes[typeName]) {
            constructorNames.push(constructorName);
        }
        return constructorNames;
    }
    constructorFields(typeName, constructorName) {
        if (!(typeName in this._primitiveTypes)) {
            throw Error('Not a primitive type: ' + typeName);
        }
        if (!(constructorName in this._primitiveTypes[typeName])) {
            throw Error('Not a primitive constructor: ' + constructorName);
        }
        return this._primitiveTypes[typeName][constructorName];
    }
    /* Operations */
    isOperation(primitiveName) {
        return (primitiveName in this._primitiveProcedures || primitiveName in this._primitiveFunctions);
    }
    getOperation(primitiveName) {
        if (primitiveName in this._primitiveProcedures) {
            return this._primitiveProcedures[primitiveName];
        }
        else if (primitiveName in this._primitiveFunctions) {
            return this._primitiveFunctions[primitiveName];
        }
        else {
            throw Error(primitiveName + ' is not a primitive.');
        }
    }
    /* Procedures */
    procedures() {
        const procedureNames = [];
        for (const procedureName in this._primitiveProcedures) {
            procedureNames.push(procedureName);
        }
        return procedureNames;
    }
    isProcedure(primitiveName) {
        return primitiveName in this._primitiveProcedures;
    }
    /* Functions */
    functions() {
        const functionNames = [];
        for (const functionName in this._primitiveFunctions) {
            functionNames.push(functionName);
        }
        return functionNames;
    }
    isFunction(primitiveName) {
        return primitiveName in this._primitiveFunctions;
    }
}

/* eslint-disable no-underscore-dangle */
/*
 * A compiler receives a symbol table (instance of SymbolTable).
 *
 * The method this.compile(ast) receives an abstract syntax tree
 * (the output of a parser).
 *
 * The AST is expected to have been linted against the given symbol table.
 *
 * The compiler produces an instance of Code, representing code for the
 * virtual machine.
 *
 * Compiling a program should never throw an exception.
 * Exceptions thrown in this module correspond to assertions,
 * i.e. internal errors that should never occur.
 * - Static conditions should be checked beforehand during the
 *   parsing and linting phases.
 * - Runtime conditions are to be checked later, during execution.
 */
class Compiler {
    constructor(symtable) {
        this._symtable = symtable;
        this._code = new Code([]);
        this._nextLabel = 0;
        this._nextVariable = 0;
        this._primitives = new RuntimePrimitives();
    }
    compile(ast) {
        this._compileMain(ast);
        return this._code;
    }
    _compileMain(ast) {
        /* Accept the empty source */
        if (ast.definitions.length === 0) {
            this._produce(ast.startPos, ast.endPos, new IReturn());
            return;
        }
        /* Compile the program (or interactive program) */
        for (const definition of ast.definitions) {
            if (definition.tag === N_DefProgram) {
                this._compileDefProgram(definition);
            }
            else if (definition.tag === N_DefInteractiveProgram) {
                this._compileDefInteractiveProgram(definition);
            }
        }
        /* Compile procedures and functions */
        for (const definition of ast.definitions) {
            if (definition.tag === N_DefProcedure) {
                this._compileDefProcedure(definition);
            }
            else if (definition.tag === N_DefFunction) {
                this._compileDefFunction(definition);
            }
        }
    }
    _compileDefProgram(definition) {
        this._compileStatement(definition.body);
        this._produce(definition.startPos, definition.endPos, new IReturn());
    }
    /* An interactive program is compiled as a switch statement
     * followed by a Return instruction. */
    _compileDefInteractiveProgram(definition) {
        this._compileMatchBranches(definition, false /* isMatching */);
        this._produce(definition.startPos, definition.endPos, new IReturn());
    }
    /* A procedure definition:
     *
     *   procedure P(x1, ..., xN) {
     *     <body>
     *   }
     *
     * is compiled as follows:
     *
     *   P:
     *     SetVariable x1
     *     ...
     *     SetVariable xN
     *     <body>
     *     Return
     */
    _compileDefProcedure(definition) {
        this._produce(definition.startPos, definition.endPos, new ILabel(definition.name.value));
        for (const parameter of definition.parameters) {
            const parameterName = parameter.value;
            this._produce(definition.startPos, definition.endPos, new ISetVariable(parameterName));
        }
        this._compileStatement(definition.body);
        this._produce(definition.startPos, definition.endPos, new IReturn());
    }
    /* A function definition:
     *
     *   function f(x1, ..., xN) {
     *     <body>
     *   }
     *
     * is compiled as follows:
     *
     *   f:
     *     SaveState
     *     SetVariable x1
     *     ...
     *     SetVariable xN
     *     <body>
     *     RestoreState
     *     Return
     */
    _compileDefFunction(definition) {
        this._produceList(definition.startPos, definition.endPos, [
            new ILabel(definition.name.value),
            new ISaveState()
        ]);
        for (const parameter of definition.parameters) {
            const parameterName = parameter.value;
            this._produce(definition.startPos, definition.endPos, new ISetVariable(parameterName));
        }
        this._compileStatement(definition.body);
        this._produceList(definition.startPos, definition.endPos, [
            new IRestoreState(),
            new IReturn()
        ]);
    }
    /* Statements are compiled to VM instructions that start and end
     * with an empty local stack. The stack may grow and shrink during the
     * execution of a statement, but it should be empty by the end.
     *
     * The only exception to this rule is the "return" statement, which
     * pushes a single value on the stack.
     */
    _compileStatement(statement) {
        switch (statement.tag) {
            case N_StmtBlock:
                return this._compileStmtBlock(statement);
            case N_StmtReturn:
                return this._compileStmtReturn(statement);
            case N_StmtIf:
                return this._compileStmtIf(statement);
            case N_StmtRepeat:
                return this._compileStmtRepeat(statement);
            case N_StmtForeach:
                return this._compileStmtForeach(statement);
            case N_StmtWhile:
                return this._compileStmtWhile(statement);
            case N_StmtSwitch:
                return this._compileStmtSwitch(statement);
            case N_StmtAssignVariable:
                return this._compileStmtAssignVariable(statement);
            case N_StmtAssignTuple:
                return this._compileStmtAssignTuple(statement);
            case N_StmtProcedureCall:
                return this._compileStmtProcedureCall(statement);
            default:
                throw Error('Compiler: Statement not implemented: ' + Symbol.keyFor(statement.tag));
        }
    }
    _compileStmtBlock(block) {
        for (const statement of block.statements) {
            this._compileStatement(statement);
        }
    }
    /* Merely push the return value in the stack.
     * The "new IReturn()" instruction itself is produced by the
     * methods:
     *   _compileDefProgram
     *   _compileDefInteractiveProgram
     *   _compileDefProcedure
     *   _compileDefFunction
     * */
    _compileStmtReturn(statement) {
        return this._compileExpression(statement.result);
    }
    /*
     * If without else:
     *
     *   <condition>
     *   TypeCheck Bool
     *   JumpIfFalse labelElse
     *   <thenBranch>
     *   labelElse:
     *
     * If with else:
     *
     *   <condition>
     *   TypeCheck Bool
     *   JumpIfFalse labelElse
     *   <thenBranch>
     *   Jump labelEnd
     *   labelElse:
     *   <elseBranch>
     *   labelEnd:
     */
    _compileStmtIf(statement) {
        this._compileExpression(statement.condition);
        this._produce(statement.condition.startPos, statement.condition.endPos, new ITypeCheck(new TypeStructure(i18n('TYPE:Bool'), {})));
        const labelElse = this._freshLabel();
        this._produce(statement.startPos, statement.endPos, new IJumpIfFalse(labelElse));
        this._compileStatement(statement.thenBlock);
        if (statement.elseBlock === undefined) {
            this._produce(statement.startPos, statement.endPos, new ILabel(labelElse));
        }
        else {
            const labelEnd = this._freshLabel();
            this._produceList(statement.startPos, statement.endPos, [
                new IJump(labelEnd),
                new ILabel(labelElse)
            ]);
            this._compileStatement(statement.elseBlock);
            this._produce(statement.startPos, statement.endPos, new ILabel(labelEnd));
        }
    }
    /* <times>
     * TypeCheck Integer
     * labelStart:
     *   Dup                     ;\
     *   PushInteger 0           ;| if not positive, end
     *   PrimitiveCall ">", 2    ;|
     *   JumpIfFalse labelEnd    ;/
     *   <body>
     *   PushInteger 1           ;\ subtract 1
     *   PrimitiveCall "-", 2    ;/
     * Jump labelStart
     * labelEnd:
     * Pop                       ; pop the remaining number
     */
    _compileStmtRepeat(statement) {
        this._compileExpression(statement.times);
        this._produce(statement.times.startPos, statement.times.endPos, new ITypeCheck(new TypeInteger()));
        const labelStart = this._freshLabel();
        const labelEnd = this._freshLabel();
        this._produceList(statement.startPos, statement.endPos, [
            new ILabel(labelStart),
            new IDup(),
            new IPushInteger(0),
            new IPrimitiveCall('>', 2),
            new IJumpIfFalse(labelEnd)
        ]);
        this._compileStatement(statement.body);
        this._produceList(statement.startPos, statement.endPos, [
            new IPushInteger(1),
            new IPrimitiveCall('-', 2),
            new IJump(labelStart),
            new ILabel(labelEnd),
            new IPop()
        ]);
    }
    /* <range>                   ;\ _list = temporary variable
     * TypeCheck List(Any)       ;| holding the list we are ranging over
     * SetVariable _list         ;/
     *
     * PushVariable _list                    ;\ _n = temporary variable
     * PrimitiveCall "_unsafeListLength", 1  ;| holding the total length
     * SetVariable _n                        ;/ of the list
     *
     * PushInteger 0             ;\ _pos = temporary variable holding the
     * SetVariable _pos          ;/ current index inside the list
     *
     * labelStart:
     *   PushVariable _pos       ;\
     *   PushVariable _n         ;| if out of the bounds of the list, end
     *   PrimitiveCall "<", 2    ;|
     *   JumpIfFalse labelEnd    ;/
     *
     *   PushVariable _list                    ;\ get the `pos`-th element of the
     *   PushVariable _pos                     ;| list and match the value
     *   PrimitiveCall "_unsafeListNth", 2     ;| with the pattern of the foreach
     *   [match with the pattern or fail]      ;/
     *
     *   <body>
     *
     *   PushVariable _pos       ;\
     *   PushInteger 1           ;| add 1 to the current index
     *   PrimitiveCall "+", 2    ;|
     *   SetVariable _pos        ;/
     *
     * Jump labelStart
     * labelEnd:
     * UnsetVariable _list
     * UnsetVariable _n
     * UnsetVariable _pos
     * [unset all the variables bound by the pattern]
     */
    _compileStmtForeach(statement) {
        const labelStart = this._freshLabel();
        const labelEnd = this._freshLabel();
        const list = this._freshVariable();
        const pos = this._freshVariable();
        const n = this._freshVariable();
        this._compileExpression(statement.range);
        this._produceList(statement.range.startPos, statement.range.endPos, [
            new ITypeCheck(new TypeList(new TypeAny())),
            new ISetVariable(list),
            new IPushVariable(list),
            new IPrimitiveCall('_unsafeListLength', 1),
            new ISetVariable(n)
        ]);
        this._produceList(statement.startPos, statement.endPos, [
            new IPushInteger(0),
            new ISetVariable(pos),
            new ILabel(labelStart),
            new IPushVariable(pos),
            new IPushVariable(n),
            new IPrimitiveCall('<', 2),
            new IJumpIfFalse(labelEnd),
            new IPushVariable(list),
            new IPushVariable(pos),
            new IPrimitiveCall('_unsafeListNth', 2)
        ]);
        this._compileMatchForeachPatternOrFail(statement.pattern);
        this._compileStatement(statement.body);
        this._produceList(statement.startPos, statement.endPos, [
            new IPushVariable(pos),
            new IPushInteger(1),
            new IPrimitiveCall('+', 2),
            new ISetVariable(pos),
            new IJump(labelStart),
            new ILabel(labelEnd),
            new IUnsetVariable(list),
            new IUnsetVariable(n),
            new IUnsetVariable(pos)
        ]);
        this._compilePatternUnbind(statement.pattern);
    }
    /* Attempt to match the pattern against the top of the stack.
     * If the pattern matches, bind its variables.
     * Otherwise, issue an error message.
     * Always pops the top of the stack.
     */
    _compileMatchForeachPatternOrFail(pattern) {
        switch (pattern.tag) {
            case N_PatternWildcard:
                this._produce(pattern.startPos, pattern.endPos, new IPop());
                return;
            case N_PatternVariable: {
                const patternVariable = pattern;
                this._produce(pattern.startPos, pattern.endPos, new ISetVariable(patternVariable.variableName.value));
                return;
            }
            default: {
                /* Attempt to match, issuing an error message if there is no match:
                 *
                 *   [if subject matches pattern, jump to L]
                 *   [error message: no match]
                 * L:
                 *   [bind pattern to subject]
                 *   [pop subject]
                 */
                const label = this._freshLabel();
                this._compilePatternCheck(pattern, label);
                this._produceList(pattern.startPos, pattern.endPos, [
                    new IPushString('foreach-pattern-does-not-match'),
                    new IPrimitiveCall('_FAIL', 1),
                    new ILabel(label)
                ]);
                this._compilePatternBind(pattern);
                this._produce(pattern.startPos, pattern.endPos, new IPop());
                return;
            }
        }
    }
    /* labelStart:
     * <condition>
     * TypeCheck Bool
     * JumpIfFalse labelEnd
     * <body>
     * Jump labelStart
     * labelEnd:
     */
    _compileStmtWhile(statement) {
        const labelStart = this._freshLabel();
        const labelEnd = this._freshLabel();
        this._produce(statement.startPos, statement.endPos, new ILabel(labelStart));
        this._compileExpression(statement.condition);
        this._produceList(statement.startPos, statement.endPos, [
            new ITypeCheck(new TypeStructure(i18n('TYPE:Bool'), {})),
            new IJumpIfFalse(labelEnd)
        ]);
        this._compileStatement(statement.body);
        this._produceList(statement.startPos, statement.endPos, [
            new IJump(labelStart),
            new ILabel(labelEnd)
        ]);
    }
    /* If the branches of the switch are:
     *    pattern1 -> body1
     *    ...      -> ...
     *    patternN -> bodyN
     * the switch construction is compiled as follows:
     *
     * <subject>
     *   [if matches pattern1, jump to label1]
     *   ...
     *   [if matches patternN, jump to labelN]
     *   [error message: no match]
     *
     * label1:
     *   [bind parameters in pattern1]
     *   [pop subject]
     *   <body1>
     *   [unbind parameters in pattern1]
     *   Jump labelEnd
     * ...
     * labelN:
     *   [bind parameters in patternN]
     *   [pop subject]
     *   <bodyN>
     *   [unbind parameters in patternN]
     *   Jump labelEnd
     * labelEnd:
     */
    _compileStmtSwitch(statement) {
        /* Compile the subject */
        this._compileExpression(statement.subject);
        this._compileMatchBranches(statement, false /* !isMatching */);
    }
    _compileMatchBranches(statement, isMatching) {
        const branchLabels = [];
        /* Attempt to match each pattern */
        for (const branch of statement.branches) {
            const label = this._freshLabel();
            branchLabels.push(label);
            this._compilePatternCheck(branch.pattern, label);
        }
        /* Issue an error message if there is no match */
        this._produceList(statement.startPos, statement.endPos, [
            new IPushString('switch-does-not-match'),
            new IPrimitiveCall('_FAIL', 1)
        ]);
        /* Compile each branch */
        const labelEnd = this._freshLabel();
        for (let i = 0; i < branchLabels.length; i++) {
            const branch = statement.branches[i];
            const label = branchLabels[i];
            this._produce(branch.startPos, branch.endPos, new ILabel(label));
            this._compilePatternBind(branch.pattern);
            this._produce(branch.startPos, branch.endPos, new IPop());
            if (isMatching) {
                this._compileExpression(branch.body);
            }
            else {
                this._compileStatement(branch.body);
            }
            this._compilePatternUnbind(branch.pattern);
            this._produce(branch.startPos, branch.endPos, new IJump(labelEnd));
        }
        this._produce(statement.startPos, statement.endPos, new ILabel(labelEnd));
    }
    _compileStmtAssignVariable(statement) {
        this._compileExpression(statement.value);
        this._produce(statement.startPos, statement.endPos, new ISetVariable(statement.variable.value));
    }
    _compileStmtAssignTuple(statement) {
        this._compileExpression(statement.value);
        /* Check that the value is indeed a tuple of the expected length */
        const anys = [];
        // eslint-disable-next-line @typescript-eslint/no-unused-vars
        for (const _variable of statement.variables) {
            anys.push(new TypeAny());
        }
        const expectedType = new TypeTuple(anys);
        this._produce(statement.startPos, statement.endPos, new ITypeCheck(expectedType));
        /* Assign each variable */
        for (let index = 0; index < statement.variables.length; index++) {
            this._produceList(statement.startPos, statement.endPos, [
                new IReadTupleComponent(index),
                new ISetVariable(statement.variables[index].value)
            ]);
        }
        /* Pop the tuple */
        this._produce(statement.startPos, statement.endPos, new IPop());
    }
    /* There are two cases:
     * (1) The procedure is a built-in primitive.
     * (2) The procedure is a user-defined procedure.
     */
    _compileStmtProcedureCall(statement) {
        const procedureName = statement.procedureName.value;
        for (const argument of statement.args) {
            this._compileExpression(argument);
        }
        if (this._primitives.isProcedure(procedureName)) {
            this._compileStmtProcedureCallPrimitive(statement);
        }
        else if (this._symtable.isProcedure(procedureName)) {
            this._compileStmtProcedureCallUserDefined(statement);
        }
        else {
            throw Error('Compiler: ' + procedureName + ' is an undefined procedure.');
        }
    }
    _compileStmtProcedureCallPrimitive(statement) {
        this._produce(statement.startPos, statement.endPos, new IPrimitiveCall(statement.procedureName.value, statement.args.length));
    }
    _compileStmtProcedureCallUserDefined(statement) {
        this._produce(statement.startPos, statement.endPos, new ICall(statement.procedureName.value, statement.args.length));
    }
    /* Pattern checks are instructions that check whether the
     * top of the stack has the expected form (matching a given pattern)
     * and, in that case, branching to the given label.
     * The top of the stack is never popped.
     * The arguments of a pattern are not bound by this instruction.
     */
    _compilePatternCheck(pattern, targetLabel) {
        switch (pattern.tag) {
            case N_PatternWildcard:
                return this._compilePatternCheckWildcard(pattern, targetLabel);
            case N_PatternVariable:
                return this._compilePatternCheckVariable(pattern, targetLabel);
            case N_PatternNumber:
                return this._compilePatternCheckNumber(pattern, targetLabel);
            case N_PatternStructure:
                return this._compilePatternCheckStructure(pattern, targetLabel);
            case N_PatternTuple:
                return this._compilePatternCheckTuple(pattern, targetLabel);
            case N_PatternTimeout:
                return this._compilePatternCheckTimeout(pattern, targetLabel);
            default:
                throw Error('Compiler: Pattern check not implemented: ' + Symbol.keyFor(pattern.tag));
        }
    }
    _compilePatternCheckWildcard(pattern, targetLabel) {
        this._produce(pattern.startPos, pattern.endPos, new IJump(targetLabel));
    }
    _compilePatternCheckVariable(pattern, targetLabel) {
        this._produce(pattern.startPos, pattern.endPos, new IJump(targetLabel));
    }
    _compilePatternCheckNumber(pattern, targetLabel) {
        this._produceList(pattern.startPos, pattern.endPos, [
            new IDup(),
            new ITypeCheck(new TypeInteger()),
            new IPushInteger(parseInt(pattern.number.value, 10)),
            new IPrimitiveCall('/=', 2),
            new IJumpIfFalse(targetLabel)
        ]);
    }
    _compilePatternCheckStructure(pattern, targetLabel) {
        /* Check that the type of the value coincides with the type
         * of the constructor */
        const constructorName = pattern.constructorName.value;
        const typeName = this._symtable.constructorType(constructorName);
        const expectedType = new TypeStructure(typeName, {});
        this._produce(pattern.startPos, pattern.endPos, new ITypeCheck(expectedType));
        /* Jump if the value matches */
        this._produce(pattern.startPos, pattern.endPos, new IJumpIfStructure(constructorName, targetLabel));
    }
    _compilePatternCheckTuple(pattern, targetLabel) {
        /* Check that the type of the value coincides with the type
         * of the tuple */
        const anys = [];
        // eslint-disable-next-line @typescript-eslint/no-unused-vars
        for (const _variable of pattern.boundVariables) {
            anys.push(new TypeAny());
        }
        const expectedType = new TypeTuple(anys);
        this._produce(pattern.startPos, pattern.endPos, new ITypeCheck(expectedType));
        /* Jump if the value matches */
        this._produce(pattern.startPos, pattern.endPos, new IJumpIfTuple(pattern.boundVariables.length, targetLabel));
    }
    _compilePatternCheckTimeout(pattern, targetLabel) {
        this._produce(pattern.startPos, pattern.endPos, new IJumpIfStructure(i18n('CONS:TIMEOUT'), targetLabel));
    }
    /* Pattern binding are instructions that bind the parameters
     * of a pattern to the corresponding parts of the value currently
     * at the top of the stack. The value at the top of the stack
     * is never popped (it must be duplicated if necessary).
     */
    _compilePatternBind(pattern) {
        switch (pattern.tag) {
            case N_PatternWildcard:
                return; /* No parameters to bind */
            case N_PatternVariable:
                this._compilePatternBindVariable(pattern);
                return;
            case N_PatternNumber:
                return; /* No parameters to bind */
            case N_PatternStructure:
                this._compilePatternBindStructure(pattern);
                return;
            case N_PatternTuple:
                this._compilePatternBindTuple(pattern);
                return;
            case N_PatternTimeout:
                return; /* No parameters to bind */
            default:
                throw Error('Compiler: Pattern binding not implemented: ' + Symbol.keyFor(pattern.tag));
        }
    }
    _compilePatternBindVariable(pattern) {
        this._produceList(pattern.startPos, pattern.endPos, [
            new IDup(),
            new ISetVariable(pattern.variableName.value)
        ]);
    }
    _compilePatternBindStructure(pattern) {
        /* Allow structure pattern with no parameters, even if the constructor
         * has parameters */
        if (pattern.boundVariables.length === 0) {
            return;
        }
        const constructorName = pattern.constructorName.value;
        const fieldNames = this._symtable.constructorFields(constructorName);
        for (let i = 0; i < fieldNames.length; i++) {
            const variable = pattern.boundVariables[i];
            const fieldName = fieldNames[i];
            this._produceList(pattern.startPos, pattern.endPos, [
                new IReadStructureField(fieldName),
                new ISetVariable(variable.value)
            ]);
        }
    }
    _compilePatternBindTuple(pattern) {
        for (let index = 0; index < pattern.boundVariables.length; index++) {
            const variable = pattern.boundVariables[index];
            this._produceList(pattern.startPos, pattern.endPos, [
                new IReadTupleComponent(index),
                new ISetVariable(variable.value)
            ]);
        }
    }
    /* Pattern unbinding are instructions that unbind the parameters
     * of a pattern. */
    _compilePatternUnbind(pattern) {
        for (const variable of pattern.boundVariables) {
            this._produceList(pattern.startPos, pattern.endPos, [
                new IUnsetVariable(variable.value)
            ]);
        }
    }
    /* Expressions are compiled to instructions that make the size
     * of the local stack grow in exactly one.
     * The stack may grow and shrink during the evaluation of an
     * expression, but an expression should not consume values
     * that were present on the stack before its evaluation started.
     * In the end the stack should have exactly one more value than
     * at the start.
     */
    _compileExpression(expression) {
        switch (expression.tag) {
            case N_ExprVariable:
                return this._compileExprVariable(expression);
            case N_ExprConstantNumber:
                return this._compileExprConstantNumber(expression);
            case N_ExprConstantString:
                return this._compileExprConstantString(expression);
            case N_ExprChoose:
                return this._compileExprChoose(expression);
            case N_ExprMatching:
                return this._compileExprMatching(expression);
            case N_ExprList:
                return this._compileExprList(expression);
            case N_ExprRange:
                return this._compileExprRange(expression);
            case N_ExprTuple:
                return this._compileExprTuple(expression);
            case N_ExprStructure:
                return this._compileExprStructure(expression);
            case N_ExprStructureUpdate:
                return this._compileExprStructureUpdate(expression);
            case N_ExprFunctionCall:
                return this._compileExprFunctionCall(expression);
            default:
                throw Error('Compiler: Expression not implemented: ' + Symbol.keyFor(expression.tag));
        }
    }
    _compileExprVariable(expression) {
        this._produce(expression.startPos, expression.endPos, new IPushVariable(expression.variableName.value));
    }
    _compileExprConstantNumber(expression) {
        this._produce(expression.startPos, expression.endPos, new IPushInteger(parseInt(expression.number.value, 10)));
    }
    _compileExprConstantString(expression) {
        this._produce(expression.startPos, expression.endPos, new IPushString(expression.string.value));
    }
    /*
     * An expression of the form:
     *
     *   choose a when (cond) b otherwise
     *
     * is compiled similarly as a statement of the form:
     *
     *   if (cond) { a } else { b }
     *
     * Recall that a 'choose' with many branches:
     *
     *   choose a1 when (cond1)
     *          ...
     *          aN when (condN)
     *          b  otherwise
     *
     * is actually parsed as a sequence of nested binary choose
     * constructions:
     *
     *   choose a1 when (cond1)
     *          (
     *            ...
     *            choose aN when (condN)
     *                    b otherwise
     *            ...
     *          ) otherwise
     *
     */
    _compileExprChoose(expression) {
        this._compileExpression(expression.condition);
        this._produce(expression.condition.startPos, expression.condition.endPos, new ITypeCheck(new TypeStructure(i18n('TYPE:Bool'), {})));
        const labelOtherwise = this._freshLabel();
        this._produce(expression.startPos, expression.endPos, new IJumpIfFalse(labelOtherwise));
        this._compileExpression(expression.trueExpr);
        const labelEnd = this._freshLabel();
        this._produceList(expression.startPos, expression.endPos, [
            new IJump(labelEnd),
            new ILabel(labelOtherwise)
        ]);
        this._compileExpression(expression.falseExpr);
        this._produce(expression.startPos, expression.endPos, new ILabel(labelEnd));
    }
    _compileExprMatching(expression) {
        this._compileExpression(expression.subject);
        this._compileMatchBranches(expression, true /* isMatching */);
    }
    _compileExprList(expression) {
        for (const element of expression.elements) {
            this._compileExpression(element);
        }
        this._produce(expression.startPos, expression.endPos, new IMakeList(expression.elements.length));
    }
    /*
     * Range expresions [first..last] and [first,second..last]
     * are compiled by calling the primitive functions
     *   _makeRange
     *   _makeRangeWithSecond
     */
    _compileExprRange(expression) {
        this._compileExpression(expression.first);
        this._compileExpression(expression.last);
        if (expression.second === undefined) {
            this._produce(expression.startPos, expression.endPos, new IPrimitiveCall('_makeRange', 2));
        }
        else {
            this._compileExpression(expression.second);
            this._produce(expression.startPos, expression.endPos, new IPrimitiveCall('_makeRangeWithSecond', 3));
        }
    }
    _compileExprTuple(expression) {
        for (const element of expression.elements) {
            this._compileExpression(element);
        }
        this._produce(expression.startPos, expression.endPos, new IMakeTuple(expression.elements.length));
    }
    _compileExprStructure(expression) {
        const fieldNames = [];
        for (const fieldBinding of expression.fieldBindings) {
            this._compileExpression(fieldBinding.value);
            fieldNames.push(fieldBinding.fieldName.value);
        }
        const constructorName = expression.constructorName.value;
        const typeName = this._symtable.constructorType(constructorName);
        this._produce(expression.startPos, expression.endPos, new IMakeStructure(typeName, constructorName, fieldNames));
    }
    _compileExprStructureUpdate(expression) {
        this._compileExpression(expression.original);
        const fieldNames = [];
        for (const fieldBinding of expression.fieldBindings) {
            this._compileExpression(fieldBinding.value);
            fieldNames.push(fieldBinding.fieldName.value);
        }
        const constructorName = expression.constructorName.value;
        const typeName = this._symtable.constructorType(constructorName);
        this._produce(expression.startPos, expression.endPos, new IUpdateStructure(typeName, constructorName, fieldNames));
    }
    /* There are four cases:
     * (1) The function is '&&' or '||' which must be considered separately
     *     to account for short-circuting.
     * (2) The function is a built-in primitive.
     * (3) The function is a user-defined function.
     * (4) The function is an observer / field accessor.
     */
    _compileExprFunctionCall(expression) {
        const functionName = expression.functionName.value;
        if (functionName === '&&') {
            this._compileExprFunctionCallAnd(expression);
        }
        else if (functionName === '||') {
            this._compileExprFunctionCallOr(expression);
        }
        else {
            for (const argument of expression.args) {
                this._compileExpression(argument);
            }
            if (this._primitives.isFunction(functionName)) {
                this._compileExprFunctionCallPrimitive(expression);
            }
            else if (this._symtable.isFunction(functionName)) {
                this._compileExprFunctionCallUserDefined(expression);
            }
            else if (this._symtable.isField(functionName)) {
                this._compileExprFunctionCallFieldAccessor(expression);
            }
            else {
                throw Error('Compiler: ' + functionName + ' is an undefined function.');
            }
        }
    }
    /* <expr1>
     * TypeCheck Bool
     * JumpIfStructure 'False' labelEnd
     * Pop
     * <expr2>
     * TypeCheck Bool
     * labelEnd:
     */
    _compileExprFunctionCallAnd(expression) {
        const expr1 = expression.args[0];
        const expr2 = expression.args[1];
        const labelEnd = this._freshLabel();
        this._compileExpression(expr1);
        this._produceList(expression.startPos, expression.endPos, [
            new ITypeCheck(new TypeStructure(i18n('TYPE:Bool'), {})),
            new IJumpIfStructure(i18n('CONS:False'), labelEnd),
            new IPop()
        ]);
        this._compileExpression(expr2);
        this._produceList(expression.startPos, expression.endPos, [
            new ITypeCheck(new TypeStructure(i18n('TYPE:Bool'), {})),
            new ILabel(labelEnd)
        ]);
    }
    /* <expr1>
     * TypeCheck Bool
     * JumpIfStructure 'True' labelEnd
     * Pop
     * <expr2>
     * TypeCheck Bool
     * labelEnd:
     */
    _compileExprFunctionCallOr(expression) {
        const expr1 = expression.args[0];
        const expr2 = expression.args[1];
        const labelEnd = this._freshLabel();
        this._compileExpression(expr1);
        this._produceList(expression.startPos, expression.endPos, [
            new ITypeCheck(new TypeStructure(i18n('TYPE:Bool'), {})),
            new IJumpIfStructure(i18n('CONS:True'), labelEnd),
            new IPop()
        ]);
        this._compileExpression(expr2);
        this._produceList(expression.startPos, expression.endPos, [
            new ITypeCheck(new TypeStructure(i18n('TYPE:Bool'), {})),
            new ILabel(labelEnd)
        ]);
    }
    _compileExprFunctionCallPrimitive(expression) {
        this._produce(expression.startPos, expression.endPos, new IPrimitiveCall(expression.functionName.value, expression.args.length));
    }
    _compileExprFunctionCallUserDefined(expression) {
        this._produce(expression.startPos, expression.endPos, new ICall(expression.functionName.value, expression.args.length));
    }
    _compileExprFunctionCallFieldAccessor(expression) {
        this._produceList(expression.startPos, expression.endPos, [
            new IReadStructureFieldPop(expression.functionName.value)
        ]);
    }
    /* Helpers */
    /* Produce the given instruction, setting its starting and ending
     * position to startPos and endPos respectively */
    _produce(startPos, endPos, instruction) {
        instruction.startPos = startPos;
        instruction.endPos = endPos;
        this._code.produce(instruction);
    }
    _produceList(startPos, endPos, instructions) {
        for (const instruction of instructions) {
            this._produce(startPos, endPos, instruction);
        }
    }
    /* Create a fresh label name */
    _freshLabel() {
        const label = '_l' + this._nextLabel.toString();
        this._nextLabel++;
        return label;
    }
    /* Create a fresh local variable name */
    _freshVariable() {
        const v = '_v' + this._nextVariable.toString();
        this._nextVariable++;
        return v;
    }
}

/* eslint-disable no-underscore-dangle */
/* Conditions that may occur on runtime */
const RT_ExitProgram = Symbol.for('RT_ExitProgram');
/* Instances of RuntimeCondition represent conditions that may occur
 * during runtime (e.g. program termination or timeout). */
class RuntimeCondition extends Error {
    constructor(tag) {
        super(Symbol.keyFor(tag));
        this.tag = tag;
    }
}
/* Runtime condition to mark the end of an execution */
class RuntimeExitProgram extends RuntimeCondition {
    constructor(returnValue) {
        super(RT_ExitProgram);
        this.returnValue = returnValue;
    }
}
function fail(startPos, endPos, reason, args) {
    throw new GbsRuntimeError(startPos, endPos, reason, args);
}
/* An instance of Frame represents the local execution context of a
 * function or procedure (a.k.a. "activation record" or "stack frame").
 *
 * It includes:
 * - the name of the current routine:
 *   + 'program' for the main program
 *   + the name of the current procedure or function
 * - the current instruction pointer
 * - a stack of local values
 * - a map from local names to values
 *
 * Each local variable has a type and a value.
 * - The actual type of the current value held by a variable
 *   should always be an instance of the type.
 * - The type of a variable should be the join of all the
 *   types held historically by the variable.
 * - The Frame does not impose these conditions.
 */
class Frame {
    constructor(frameId, routineName, instructionPointer) {
        this._routineName = routineName;
        this._instructionPointer = instructionPointer;
        this._variableTypes = {};
        this._variables = {};
        this._stack = [];
        /* The unique frame identifier is used to uniquely identify
         * a function call during a stack trace. This is used in the
         * API to generate snapshots. */
        this._uniqueFrameId = frameId;
    }
    get routineName() {
        return this._routineName;
    }
    get uniqueFrameId() {
        return this._uniqueFrameId;
    }
    get instructionPointer() {
        return this._instructionPointer;
    }
    set instructionPointer(value) {
        this._instructionPointer = value;
    }
    /* Precondition:
     *   Let oldType = this._variableTypes[name]
     *   if this._variableTypes[name] is defined.
     *   Otherwise, let oldType = new TypeAny().
     *   Then the following condition must hold:
     *     type = joinTypes(value.type(), oldType) */
    setVariable(name, type, value) {
        this._variableTypes[name] = type;
        this._variables[name] = value;
    }
    unsetVariable(name) {
        delete this._variables[name];
    }
    getVariableType(name) {
        if (name in this._variableTypes) {
            return this._variableTypes[name];
        }
        else {
            return new TypeAny();
        }
    }
    getVariable(name) {
        if (name in this._variables) {
            return this._variables[name];
        }
        else {
            return undefined;
        }
    }
    stackEmpty() {
        return this._stack.length === 0;
    }
    pushValue(value) {
        this._stack.push(value);
    }
    stackTop() {
        if (this._stack.length === 0) {
            throw Error('VM: no value at the top of the stack; the stack is empty.');
        }
        return this._stack[this._stack.length - 1];
    }
    popValue() {
        if (this._stack.length === 0) {
            throw Error('VM: no value to pop; the stack is empty.');
        }
        return this._stack.pop();
    }
}
/*
 * Receives an instance of Code, representing a program for the virtual
 * machine, and sets it up for running.
 *
 * Then it implements the following interface:
 *
 *   vm.run();    Run the program until termination.
 *                If the program returns a value, this method
 *                returns it. Otherwise it returns undefined.
 */
class VirtualMachine {
    constructor(code, initialState) {
        this._code = code;
        /* "this._labelTargets" is a dictionary mapping label names to
         * the corresponding instruction pointers.
         *
         * It is calculated automatically from code.
         */
        this._labelTargets = this._code.labelTargets();
        this._nextFrameId = 0;
        /* A "call stack" is a stack of frames.
         *
         * The topmost element of the stack (i.e. the last element of the list)
         * is the execution context of the current function.
         *
         * The previous element is the execution context of the caller, and so on.
         *
         * During the execution of a program the call stack should never
         * become empty.
         */
        this._callStack = [];
        this._callStack.push(this._newFrame('program', 0 /* instructionPointer */));
        /* The global state is the data that is available globally.
         *
         * In Gobstones, the global state is the board. The VM module
         * should not be aware of the actual implementation or nature of
         * the global state.
         *
         * We have a stack of global states.
         *
         * The instruction 'SaveState' saves the current global state.
         * It should be called whenever entering a user-defined function
         * in Gobstones.
         *
         * The instruction 'RestoreState' restores the previous global state.
         * It should be called whenever leaving a user-defined function
         * in Gobstones.
         */
        this._globalStateStack = [initialState];
        /* The following dictionary maps names of primitives to their
         * implementation.
         *
         * A primitive always receives 1 + n parameters, the first one being
         * the board.
         */
        this._primitives = new RuntimePrimitives();
        /*
         * A "snapshot callback" is a function that takes snapshots.
         *
         *   snapshotCallback(routineName, position, callStack, globalState)
         *
         *   routineName:
         *     It is the name of the routine that triggers the
         *     snapshot, it might be:
         *     - 'program' for the main program,
         *     - the name of a primitive procedure or function,
         *     - the name of a user-defined procedure or function.
         *
         *   position:
         *     The position in the source code for this snapshot.
         *
         *   callStack:
         *     The current call stack.
         *
         *   globalState:
         *     The current global state.
         *
         * Snapshots
         * If _snapshotCallback is undefined, the VM does not take snapshots.
         */
        this._snapshotCallback = undefined;
    }
    run() {
        return this.runWithTimeout(0);
    }
    /* Run the program, throwing an exception if the given timeout is met.
     * If millisecs is 0, the program is run indefinitely. */
    runWithTimeout(millisecs) {
        return this.runWithTimeoutTakingSnapshots(millisecs, undefined);
    }
    /* Restart the program from the beginning, with the given eventValue
     * at the top of the stack.
     *
     * This is used for interactive programs, which work by iteratively
     * making calls to this function.
     */
    runEventWithTimeout(eventValue, millisecs) {
        this._callStack = [this._newFrame('program', 0 /* instructionPointer */)];
        this._currentFrame().pushValue(eventValue);
        return this.runWithTimeout(millisecs);
    }
    /* Run the program, throwing an exception if the given timeout is met.
     * If millisecs is 0, the program is run indefinitely.
     *
     * Snapshots are taken:
     * - At the very start of the program.
     * - At the end of the program.
     * - After calling any primitive procedure or function.
     * - Whenever reaching an I_Return instruction from any routine.
     *
     * The snapshotCallback function receives:
     * - The current call stack (list of frames).
     * - The current global state.
     */
    // eslint-disable-next-line @typescript-eslint/ban-types
    runWithTimeoutTakingSnapshots(millisecs, snapshotCallback) {
        const startTime = new Date().getTime();
        this._snapshotCallback = snapshotCallback;
        this._takeSnapshot('program');
        try {
            // eslint-disable-next-line no-constant-condition
            while (true) {
                this._step();
                this._timeoutIfNeeded(startTime, millisecs);
            }
        }
        catch (condition) {
            if (condition.tag === RT_ExitProgram) {
                return condition.returnValue;
            }
            else {
                throw condition;
            }
        }
    }
    _newFrame(routineName, instructionPointer) {
        const frameId = this._nextFrameId;
        this._nextFrameId++;
        return new Frame(frameId, routineName, instructionPointer);
    }
    _timeoutIfNeeded(startTime, millisecs) {
        if (millisecs > 0 && new Date().getTime() - startTime > millisecs) {
            const instruction = this._currentInstruction();
            fail(instruction.startPos, instruction.endPos, 'timeout', [millisecs]);
        }
    }
    _takeSnapshot(routineName) {
        if (this._snapshotCallback !== undefined) {
            const instruction = this._currentInstruction();
            this._snapshotCallback(routineName, instruction.startPos, this._callStack, this.globalState());
        }
    }
    globalState() {
        return this._globalStateStack[this._globalStateStack.length - 1];
    }
    setGlobalState(globalState) {
        this._globalStateStack[this._globalStateStack.length - 1] = globalState;
    }
    /* Return the current frame, which is the top of the call stack */
    _currentFrame() {
        return this._callStack[this._callStack.length - 1];
    }
    /* Return the current instruction, given by the instruction pointer
     * of the current activation record */
    _currentInstruction() {
        return this._code.at(this._currentFrame().instructionPointer);
    }
    /* Execute a single instruction.
     *
     * If the program finishes, it throws an exception
     *   RuntimeExitProgram(returnValue)
     */
    _step() {
        switch (this._currentInstruction().opcode) {
            case I_PushInteger:
                return this._stepPushInteger();
            case I_PushString:
                return this._stepPushString();
            case I_PushVariable:
                return this._stepPushVariable();
            case I_SetVariable:
                return this._stepSetVariable();
            case I_UnsetVariable:
                return this._stepUnsetVariable();
            case I_Label:
                return this._stepLabel();
            case I_Jump:
                return this._stepJump();
            case I_JumpIfFalse:
                return this._stepJumpIfFalse();
            case I_JumpIfStructure:
                return this._stepJumpIfStructure();
            case I_JumpIfTuple:
                return this._stepJumpIfTuple();
            case I_Call:
                return this._stepCall();
            case I_Return:
                return this._stepReturn();
            case I_MakeTuple:
                return this._stepMakeTuple();
            case I_MakeList:
                return this._stepMakeList();
            case I_MakeStructure:
                return this._stepMakeStructure();
            case I_UpdateStructure:
                return this._stepUpdateStructure();
            case I_ReadTupleComponent:
                return this._stepReadTupleComponent();
            case I_ReadStructureField:
                return this._stepReadStructureField();
            case I_ReadStructureFieldPop:
                return this._stepReadStructureFieldPop();
            case I_Add:
                return this._stepAdd();
            case I_Dup:
                return this._stepDup();
            case I_Pop:
                return this._stepPop();
            case I_PrimitiveCall:
                return this._stepPrimitiveCall();
            case I_SaveState:
                return this._stepSaveState();
            case I_RestoreState:
                return this._stepRestoreState();
            case I_TypeCheck:
                return this._stepTypeCheck();
            default:
                throw Error('VM: opcode ' +
                    Symbol.keyFor(this._currentInstruction().opcode) +
                    ' not implemented');
        }
    }
    _stepPushInteger() {
        const frame = this._currentFrame();
        const instruction = this._currentInstruction();
        frame.pushValue(new ValueInteger(instruction.number));
        frame.instructionPointer++;
    }
    _stepPushString() {
        const frame = this._currentFrame();
        const instruction = this._currentInstruction();
        frame.pushValue(new ValueString(instruction.string));
        frame.instructionPointer++;
    }
    _stepPushVariable() {
        const frame = this._currentFrame();
        const instruction = this._currentInstruction();
        const value = frame.getVariable(instruction.variableName);
        if (value === undefined) {
            fail(instruction.startPos, instruction.endPos, 'undefined-variable', [
                instruction.variableName
            ]);
        }
        frame.pushValue(value);
        frame.instructionPointer++;
    }
    _stepSetVariable() {
        const frame = this._currentFrame();
        const instruction = this._currentInstruction();
        const newValue = frame.popValue();
        /* Check that types are compatible */
        const oldType = frame.getVariableType(instruction.variableName);
        const valType = newValue.type();
        const newType = joinTypes(oldType, valType);
        if (newType === undefined) {
            fail(instruction.startPos, instruction.endPos, 'incompatible-types-on-assignment', [
                instruction.variableName,
                oldType,
                valType
            ]);
        }
        /* Proceed with assignment */
        frame.setVariable(instruction.variableName, newType, newValue);
        frame.instructionPointer++;
    }
    _stepUnsetVariable() {
        const frame = this._currentFrame();
        const instruction = this._currentInstruction();
        frame.unsetVariable(instruction.variableName);
        frame.instructionPointer++;
    }
    _stepLabel() {
        /* Ignore pseudo-instruction */
        const frame = this._currentFrame();
        frame.instructionPointer++;
    }
    _stepJump() {
        const frame = this._currentFrame();
        const instruction = this._currentInstruction();
        frame.instructionPointer = this._labelTargets[instruction.targetLabel];
    }
    _stepJumpIfFalse() {
        const frame = this._currentFrame();
        const instruction = this._currentInstruction();
        const value = frame.popValue(); /* Pop the value */
        if (value.tag === V_Structure && value.constructorName === 'False') {
            frame.instructionPointer = this._labelTargets[instruction.targetLabel];
        }
        else {
            frame.instructionPointer++;
        }
    }
    _stepJumpIfStructure() {
        const frame = this._currentFrame();
        const instruction = this._currentInstruction();
        const value = frame.stackTop(); /* Do not pop the value */
        if (value.tag === V_Structure && value.constructorName === instruction.constructorName) {
            frame.instructionPointer = this._labelTargets[instruction.targetLabel];
        }
        else {
            frame.instructionPointer++;
        }
    }
    _stepJumpIfTuple() {
        const frame = this._currentFrame();
        const instruction = this._currentInstruction();
        const value = frame.stackTop(); /* Do not pop the value */
        if (value.tag === V_Tuple && value.size() === instruction.size) {
            frame.instructionPointer = this._labelTargets[instruction.targetLabel];
        }
        else {
            frame.instructionPointer++;
        }
    }
    _stepCall() {
        const callerFrame = this._currentFrame();
        const instruction = this._currentInstruction();
        /* Create a new stack frame for the callee */
        const newFrame = this._newFrame(instruction.targetLabel, this._labelTargets[instruction.targetLabel]);
        this._callStack.push(newFrame);
        /* Pop arguments from caller's frame and push them into callee's frame */
        for (let i = 0; i < instruction.nargs; i++) {
            if (callerFrame.stackEmpty()) {
                fail(instruction.startPos, instruction.endPos, 'too-few-arguments', [
                    instruction.targetLabel
                ]);
            }
            newFrame.pushValue(callerFrame.popValue());
        }
    }
    _stepReturn() {
        const innerFrame = this._currentFrame();
        let returnValue;
        if (innerFrame.stackEmpty()) {
            returnValue = undefined;
        }
        else {
            /* Take a snapshot when leaving a routine other than the program */
            this._takeSnapshot(innerFrame.routineName);
            returnValue = innerFrame.popValue();
            if (!innerFrame.stackEmpty()) {
                throw Error('VM: stack should be empty');
            }
        }
        this._callStack.pop();
        if (this._callStack.length === 0) {
            /* There are no more frames in the call stack, which means
             * that we are returning from the main program. */
            throw new RuntimeExitProgram(returnValue);
        }
        else {
            /* There are further frames in the call stack, which means
             * that we are returning from a function. */
            const outerFrame = this._currentFrame();
            if (returnValue !== undefined) {
                outerFrame.pushValue(returnValue);
            }
            outerFrame.instructionPointer++;
        }
    }
    _stepMakeTuple() {
        const frame = this._currentFrame();
        const instruction = this._currentInstruction();
        const elements = [];
        for (let i = 0; i < instruction.size; i++) {
            elements.unshift(frame.popValue());
        }
        frame.pushValue(new ValueTuple(elements));
        frame.instructionPointer++;
    }
    _stepMakeList() {
        const frame = this._currentFrame();
        const instruction = this._currentInstruction();
        const elements = [];
        for (let i = 0; i < instruction.size; i++) {
            elements.unshift(frame.popValue());
        }
        /* Check that the types of the elements are compatible */
        let contentType = new TypeAny();
        let index = 0;
        for (const element of elements) {
            const oldType = contentType;
            const newType = element.type();
            contentType = joinTypes(oldType, newType);
            if (contentType === undefined) {
                fail(instruction.startPos, instruction.endPos, 'incompatible-types-on-list-creation', [index, oldType, newType]);
            }
            index++;
        }
        frame.pushValue(new ValueList(elements));
        frame.instructionPointer++;
    }
    _stepMakeStructure() {
        const frame = this._currentFrame();
        const instruction = this._currentInstruction();
        const fields = {};
        const n = instruction.fieldNames.length;
        for (let i = 0; i < n; i++) {
            const fieldName = instruction.fieldNames[n - i - 1];
            fields[fieldName] = frame.popValue();
        }
        frame.pushValue(new ValueStructure(instruction.typeName, instruction.constructorName, fields));
        frame.instructionPointer++;
    }
    _stepUpdateStructure() {
        const frame = this._currentFrame();
        const instruction = this._currentInstruction();
        const newFields = {};
        const newFieldNames = [];
        const n = instruction.fieldNames.length;
        for (let i = 0; i < n; i++) {
            const fieldName = instruction.fieldNames[n - i - 1];
            newFields[fieldName] = frame.popValue();
            newFieldNames.unshift(fieldName);
        }
        /* Check that it is a structure and built with the same constructor */
        const structure = frame.popValue();
        if (structure.tag !== V_Structure) {
            fail(instruction.startPos, instruction.endPos, 'expected-structure-but-got', [
                instruction.constructorName,
                i18n(Symbol.keyFor(structure.tag))
            ]);
        }
        if (structure.constructorName !== instruction.constructorName) {
            fail(instruction.startPos, instruction.endPos, 'expected-constructor-but-got', [
                instruction.constructorName,
                structure.constructorName
            ]);
        }
        if (structure.typeName !== instruction.typeName) {
            throw Error('VM: UpdateStructure instruction does not match type.');
        }
        /* Check that the types of the fields are compatible */
        for (const fieldName of newFieldNames) {
            const oldType = structure.fields[fieldName].type();
            const newType = newFields[fieldName].type();
            if (joinTypes(oldType, newType) === undefined) {
                fail(instruction.startPos, instruction.endPos, 'incompatible-types-on-structure-update', [fieldName, oldType, newType]);
            }
        }
        /* Proceed with structure update */
        frame.pushValue(structure.updateFields(newFields));
        frame.instructionPointer++;
    }
    _stepReadTupleComponent() {
        const frame = this._currentFrame();
        const instruction = this._currentInstruction();
        const tuple = frame.stackTop();
        if (tuple.tag !== V_Tuple) {
            fail(instruction.startPos, instruction.endPos, 'expected-tuple-value-but-got', [
                tuple.type()
            ]);
        }
        if (instruction.index >= tuple.size()) {
            fail(instruction.startPos, instruction.endPos, 'tuple-component-out-of-bounds', [
                tuple.size(),
                instruction.index
            ]);
        }
        frame.pushValue(tuple.components[instruction.index]);
        frame.instructionPointer++;
    }
    _stepReadStructureFieldGeneric(shouldPopStructure) {
        const frame = this._currentFrame();
        const instruction = this._currentInstruction();
        let structure;
        if (shouldPopStructure) {
            structure = frame.popValue();
        }
        else {
            structure = frame.stackTop();
        }
        if (structure.tag !== V_Structure) {
            fail(instruction.startPos, instruction.endPos, 'expected-structure-value-but-got', [
                structure.type()
            ]);
        }
        if (!(instruction.fieldName in structure.fields)) {
            fail(instruction.startPos, instruction.endPos, 'structure-field-not-present', [
                structure.fieldNames(),
                instruction.fieldName
            ]);
        }
        frame.pushValue(structure.fields[instruction.fieldName]);
        frame.instructionPointer++;
    }
    _stepReadStructureField() {
        this._stepReadStructureFieldGeneric(false); /* Do not pop the structure */
    }
    _stepReadStructureFieldPop() {
        this._stepReadStructureFieldGeneric(true); /* Pop the structure */
    }
    /* Instruction used for testing/debugging */
    _stepAdd() {
        const frame = this._currentFrame();
        const v1 = frame.popValue();
        const v2 = frame.popValue();
        frame.pushValue(v1.add(v2));
        frame.instructionPointer++;
    }
    _stepDup() {
        const frame = this._currentFrame();
        const value = frame.popValue();
        frame.pushValue(value);
        frame.pushValue(value);
        frame.instructionPointer++;
    }
    _stepPop() {
        const frame = this._currentFrame();
        frame.popValue();
        frame.instructionPointer++;
    }
    _stepPrimitiveCall() {
        const frame = this._currentFrame();
        const instruction = this._currentInstruction();
        /* Pop arguments from stack */
        const args = [];
        for (let i = 0; i < instruction.nargs; i++) {
            args.unshift(frame.popValue());
        }
        /* Check that the primitive exists */
        if (!this._primitives.isOperation(instruction.primitiveName)) {
            fail(instruction.startPos, instruction.endPos, 'primitive-does-not-exist', [
                instruction.primitiveName
            ]);
        }
        const primitive = this._primitives.getOperation(instruction.primitiveName);
        /* Check that the number of expected parameters coincides with
         * the actual arguments provided */
        if (primitive.argumentTypes.length !== instruction.nargs) {
            fail(instruction.startPos, instruction.endPos, 'primitive-arity-mismatch', [
                instruction.primitiveName,
                primitive.argumentTypes.length,
                instruction.nargs
            ]);
        }
        /* Check that the types of all parameters coincide with the types of the
         * actual arguments */
        for (let i = 0; i < instruction.nargs; i++) {
            const expectedType = primitive.argumentTypes[i];
            const receivedType = args[i].type();
            if (joinTypes(expectedType, receivedType) === undefined) {
                fail(instruction.startPos, instruction.endPos, 'primitive-argument-type-mismatch', [
                    instruction.primitiveName,
                    i + 1,
                    instruction.nargs,
                    expectedType,
                    receivedType
                ]);
            }
        }
        /* Validate the arguments using the primitive-specific validator */
        primitive.validateArguments(instruction.startPos, instruction.endPos, this.globalState(), args);
        /* Proceed to call the primitive operation */
        const result = primitive.call(this.globalState(), args); /* mutates 'args' */
        if (result !== undefined) {
            frame.pushValue(result);
        }
        /* Take a snapshot after calling the primitive operation */
        this._takeSnapshot(instruction.primitiveName);
        frame.instructionPointer++;
    }
    _stepSaveState() {
        const frame = this._currentFrame();
        this._globalStateStack.push(this.globalState().clone());
        frame.instructionPointer++;
    }
    _stepRestoreState() {
        const frame = this._currentFrame();
        this._globalStateStack.pop();
        if (this._globalStateStack.length === 0) {
            throw Error('RestoreState: the stack of global states is empty.');
        }
        frame.instructionPointer++;
    }
    _stepTypeCheck() {
        const frame = this._currentFrame();
        const instruction = this._currentInstruction();
        const expectedType = instruction.type;
        const receivedType = frame.stackTop().type();
        if (joinTypes(expectedType, receivedType) === undefined) {
            fail(instruction.startPos, instruction.endPos, 'expected-value-of-type-but-got', [
                expectedType,
                receivedType
            ]);
        }
        frame.instructionPointer++;
    }
    /* Return the current dynamic stack of regions */
    regionStack() {
        const regionStack = [];
        for (const stackFrame of this._callStack) {
            const instruction = this._code.at(stackFrame.instructionPointer);
            regionStack.push(instruction.startPos.region);
        }
        return regionStack;
    }
}

/* eslint-disable no-underscore-dangle */
/* This module is a façade for all the combined functionality of the
 * parser/compiler/vm
 */
const tok = (tag, value) => new Token(tag, value, UnknownPosition, UnknownPosition);
class Runner {
    constructor() {
        this.initialize();
    }
    initialize() {
        this._ast = undefined;
        this._primitives = new RuntimePrimitives();
        this._symtable = this._newSymtableWithPrimitives();
        this._linter = new Linter(this._symtable);
        this._code = undefined;
        this._vm = undefined;
        this._result = undefined;
    }
    /* Parse, compile, and run a program in the default global state
     * (typically an empty 9x9 board in Gobstones).
     * Return the return value of the program, ignoring the final state.
     * A GbsInterpreterException may be thrown.
     */
    run(input) {
        return this.runState(input, new RuntimeState()).result;
    }
    /* Parse, compile, and run a program in the given initial state.
     * Return an object of the form
     *   {'result': r, 'state': s]
     * where r is the result of the program and s is the final state.
     * A GbsInterpreterException may be thrown.
     */
    runState(input, initialState) {
        this.parse(input);
        this.lint();
        this.compile();
        this.execute(initialState);
        return { result: this._result, state: this._vm.globalState() };
    }
    parse(input) {
        const parser = new Parser(input);
        this._ast = parser.parse();
        for (const option of parser.getLanguageOptions()) {
            this._setLanguageOption(option);
        }
    }
    enableLintCheck(linterCheckId, enabled) {
        this._linter.enableCheck(linterCheckId, enabled);
    }
    lint() {
        this._symtable = this._linter.lint(this._ast);
    }
    compile() {
        this._code = new Compiler(this._symtable).compile(this._ast);
    }
    initializeVirtualMachine(initialState) {
        this._vm = new VirtualMachine(this._code, initialState);
    }
    execute(initialState) {
        this.executeWithTimeout(initialState, 0);
    }
    executeWithTimeout(initialState, millisecs) {
        this.executeWithTimeoutTakingSnapshots(initialState, millisecs, undefined);
    }
    executeWithTimeoutTakingSnapshots(initialState, millisecs, 
    // eslint-disable-next-line @typescript-eslint/ban-types
    snapshotCallback) {
        this.initializeVirtualMachine(initialState);
        this._result = this._vm.runWithTimeoutTakingSnapshots(millisecs, snapshotCallback);
    }
    executeEventWithTimeout(eventValue, millisecs) {
        this._result = this._vm.runEventWithTimeout(eventValue, millisecs);
    }
    get abstractSyntaxTree() {
        return this._ast;
    }
    get primitives() {
        return this._primitives;
    }
    get symbolTable() {
        return this._symtable;
    }
    get virtualMachineCode() {
        return this._code;
    }
    get result() {
        return this._result;
    }
    get globalState() {
        return this._vm.globalState();
    }
    /* Evaluate language options set by the LANGUAGE pragma */
    _setLanguageOption(option) {
        if (option === 'DestructuringForeach') {
            this.enableLintCheck('forbidden-extension-destructuring-foreach', false);
        }
        else if (option === 'AllowRecursion') {
            this.enableLintCheck('forbidden-extension-allow-recursion', false);
        }
        else {
            throw Error('Unknown language option: ' + option);
        }
    }
    /* Dynamic stack of regions */
    regionStack() {
        return this._vm.regionStack();
    }
    /* Create a new symbol table, including definitions for all the primitive
     * types and operations (which come from RuntimePrimitives) */
    _newSymtableWithPrimitives() {
        const symtable = new SymbolTable();
        /* Populate symbol table with primitive types */
        for (const type of this._primitives.types()) {
            symtable.defType(this._astDefType(type));
        }
        /* Populate symbol table with primitive procedures */
        for (const procedureName of this._primitives.procedures()) {
            symtable.defProcedure(this._astDefProcedure(procedureName));
        }
        /* Populate symbol table with primitive functions */
        for (const functionName of this._primitives.functions()) {
            symtable.defFunction(this._astDefFunction(functionName));
        }
        return symtable;
    }
    _astDefType(type) {
        const constructorDeclarations = [];
        for (const constructor of this._primitives.typeConstructors(type)) {
            constructorDeclarations.push(this._astConstructorDeclaration(type, constructor));
        }
        return new ASTDefType(tok(T_UPPERID, type), constructorDeclarations);
    }
    _astDefProcedure(procedureName) {
        const nargs = this._primitives.getOperation(procedureName).nargs();
        const parameters = [];
        for (let i = 1; i <= nargs; i++) {
            parameters.push(tok(T_LOWERID, 'x' + i.toString()));
        }
        return new ASTDefProcedure(tok(T_LOWERID, procedureName), parameters, new ASTStmtBlock([]));
    }
    _astDefFunction(functionName) {
        const nargs = this._primitives.getOperation(functionName).nargs();
        const parameters = [];
        for (let i = 1; i <= nargs; i++) {
            parameters.push(tok(T_LOWERID, 'x' + i.toString()));
        }
        return new ASTDefFunction(tok(T_LOWERID, functionName), parameters, new ASTStmtBlock([]));
    }
    _astConstructorDeclaration(type, constructor) {
        const fields = [];
        for (const field of this._primitives.constructorFields(type, constructor)) {
            fields.push(tok(T_LOWERID, field));
        }
        return new ASTConstructorDeclaration(tok(T_UPPERID, constructor), fields);
    }
}

export { Code, Compiler, Frame, IAdd, ICall, IDup, IJump, IJumpIfFalse, IJumpIfStructure, IJumpIfTuple, ILabel, IMakeList, IMakeStructure, IMakeTuple, IPop, IPrimitiveCall, IPushInteger, IPushString, IPushVariable, IReadStructureField, IReadStructureFieldPop, IReadTupleComponent, IRestoreState, IReturn, ISaveState, ISetVariable, ITypeCheck, IUnsetVariable, IUpdateStructure, I_Add, I_Call, I_Dup, I_Jump, I_JumpIfFalse, I_JumpIfStructure, I_JumpIfTuple, I_Label, I_MakeList, I_MakeStructure, I_MakeTuple, I_Pop, I_PrimitiveCall, I_PushInteger, I_PushString, I_PushVariable, I_ReadStructureField, I_ReadStructureFieldPop, I_ReadTupleComponent, I_RestoreState, I_Return, I_SaveState, I_SetVariable, I_TypeCheck, I_UnsetVariable, I_UpdateStructure, Instruction, Runner, RuntimePrimitives, RuntimeState, Type, TypeAny, TypeInteger, TypeList, TypeString, TypeStructure, TypeTuple, V_Integer, V_List, V_String, V_Structure, V_Tuple, Value, ValueInteger, ValueList, ValueString, ValueStructure, ValueTuple, VirtualMachine, boolFromValue, joinTypes, typesWithOpposite, typesWithOrder };
//# sourceMappingURL=index.js.map
