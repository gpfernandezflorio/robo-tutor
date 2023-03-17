export declare class Type {
    private _tag;
    constructor(tag: symbol);
    get tag(): symbol;
    isAny(): boolean;
    isInteger(): boolean;
    isString(): boolean;
    isTuple(): boolean;
    isList(): boolean;
    isStructure(): boolean;
    isBoolean(): boolean;
    isColor(): boolean;
    isDirection(): boolean;
}
export declare class TypeAny extends Type {
    constructor();
    toString(): string;
    isAny(): boolean;
}
export declare class TypeInteger extends Type {
    constructor();
    toString(): string;
    isInteger(): boolean;
}
export declare class TypeString extends Type {
    constructor();
    toString(): string;
    isString(): boolean;
}
export declare class TypeTuple extends Type {
    private _componentTypes;
    constructor(componentTypes: Type[]);
    get componentTypes(): Type[];
    toString(): string;
    isTuple(): boolean;
}
export declare class TypeList extends Type {
    private _contentType;
    constructor(contentType: Type);
    get contentType(): Type;
    toString(): string;
    isList(): boolean;
}
export declare class TypeStructure extends Type {
    private _typeName;
    private _cases;
    constructor(typeName: string, cases: Record<string, Record<string, Type>>);
    get typeName(): string;
    get cases(): Record<string, Record<string, Type>>;
    toString(): string;
    isStructure(): boolean;
    isBoolean(): boolean;
    isColor(): boolean;
    isDirection(): boolean;
}
export declare function joinTypes(type1: Type, type2: Type): Type;
export declare const V_Integer: unique symbol;
export declare const V_String: unique symbol;
export declare const V_Tuple: unique symbol;
export declare const V_List: unique symbol;
export declare const V_Structure: unique symbol;
export declare class Value {
    private _tag;
    constructor(tag: symbol);
    get tag(): symbol;
    type(): Type;
    isInteger(): boolean;
    isString(): boolean;
    isTuple(): boolean;
    isList(): boolean;
    isStructure(): boolean;
    isBoolean(): boolean;
    equal(other: Value): boolean;
}
export declare class ValueInteger extends Value {
    private _number;
    constructor(number: number | string);
    toString(): string;
    get number(): number;
    type(): Type;
    equal(other: Value): boolean;
    add(other: ValueInteger): ValueInteger;
    sub(other: ValueInteger): ValueInteger;
    mul(other: ValueInteger): ValueInteger;
    div(other: ValueInteger): ValueInteger;
    mod(other: ValueInteger): ValueInteger;
    pow(other: ValueInteger): ValueInteger;
    eq(other: ValueInteger): boolean;
    ne(other: ValueInteger): boolean;
    le(other: ValueInteger): boolean;
    lt(other: ValueInteger): boolean;
    ge(other: ValueInteger): boolean;
    gt(other: ValueInteger): boolean;
    negate(): ValueInteger;
    abs(): ValueInteger;
    asNumber(): number;
}
export declare class ValueString extends Value {
    private _string;
    constructor(string: string);
    toString(): string;
    get string(): string;
    equal(other: Value): boolean;
    type(): Type;
}
export declare class ValueTuple extends Value {
    private _components;
    private _type;
    constructor(components: Value[]);
    toString(): string;
    get components(): Value[];
    size(): number;
    equal(other: Value): boolean;
    type(): Type;
    _inferType(): TypeTuple;
}
export declare class ValueList extends Value {
    private _elements;
    private _type;
    constructor(elements: Value[]);
    toString(): string;
    get elements(): Value[];
    equal(other: Value): boolean;
    type(): Type;
    length(): number;
    _inferType(): Type;
    append(other: ValueList): ValueList;
    head(): Value;
    tail(): ValueList;
    init(): ValueList;
    last(): Value;
}
export declare class ValueStructure extends Value {
    private _typeName;
    private _constructorName;
    private _fields;
    constructor(typeName: string, constructorName: string, fields: Record<string, Value>);
    toString(): string;
    get typeName(): string;
    get constructorName(): string;
    get fields(): Record<string, Value>;
    fieldNames(): string[];
    _clone(): ValueStructure;
    updateFields(fields: Record<string, Value>): ValueStructure;
    equal(other: Value): boolean;
    type(): Type;
}
//# sourceMappingURL=value.d.ts.map