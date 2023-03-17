import { SourceReader } from '@gobstones/gobstones-parser';
import { Type } from './value';
export declare const I_PushInteger: unique symbol;
export declare const I_PushString: unique symbol;
export declare const I_PushVariable: unique symbol;
export declare const I_SetVariable: unique symbol;
export declare const I_UnsetVariable: unique symbol;
export declare const I_Label: unique symbol;
export declare const I_Jump: unique symbol;
export declare const I_JumpIfFalse: unique symbol;
export declare const I_JumpIfStructure: unique symbol;
export declare const I_JumpIfTuple: unique symbol;
export declare const I_Call: unique symbol;
export declare const I_Return: unique symbol;
export declare const I_MakeTuple: unique symbol;
export declare const I_MakeList: unique symbol;
export declare const I_MakeStructure: unique symbol;
export declare const I_UpdateStructure: unique symbol;
export declare const I_ReadTupleComponent: unique symbol;
export declare const I_ReadStructureField: unique symbol;
export declare const I_ReadStructureFieldPop: unique symbol;
export declare const I_Add: unique symbol;
export declare const I_Dup: unique symbol;
export declare const I_Pop: unique symbol;
export declare const I_PrimitiveCall: unique symbol;
export declare const I_SaveState: unique symbol;
export declare const I_RestoreState: unique symbol;
export declare const I_TypeCheck: unique symbol;
export declare class Code {
    private _instructions;
    constructor(instructions: Instruction[]);
    toString(): string;
    produce(instruction: Instruction): void;
    at(ip: number): Instruction;
    labelTargets(): Record<string, number>;
}
export declare class Instruction {
    _opcode: symbol;
    _args: any[];
    _startPos: SourceReader;
    _endPos: SourceReader;
    constructor(opcode: symbol, args: any[]);
    toString(): string;
    get opcode(): symbol;
    get args(): string[];
    set startPos(position: SourceReader);
    get startPos(): SourceReader;
    set endPos(position: SourceReader);
    get endPos(): SourceReader;
}
export declare class IPushInteger extends Instruction {
    constructor(number: number);
    get number(): number;
}
export declare class IPushString extends Instruction {
    constructor(string: string);
    get string(): string;
}
export declare class IPushVariable extends Instruction {
    constructor(variableName: string);
    get variableName(): string;
}
export declare class ISetVariable extends Instruction {
    constructor(variableName: string);
    get variableName(): string;
}
export declare class IUnsetVariable extends Instruction {
    constructor(variableName: string);
    get variableName(): string;
}
export declare class ILabel extends Instruction {
    constructor(label: string);
    toString(): string;
    get label(): string;
}
export declare class IJump extends Instruction {
    constructor(targetLabel: string);
    get targetLabel(): string;
}
export declare class IJumpIfFalse extends Instruction {
    constructor(targetLabel: string);
    get targetLabel(): string;
}
export declare class IJumpIfStructure extends Instruction {
    constructor(constructorName: string, targetLabel: string);
    get constructorName(): string;
    get targetLabel(): string;
}
export declare class IJumpIfTuple extends Instruction {
    constructor(size: number, targetLabel: string);
    get size(): number;
    get targetLabel(): string;
}
export declare class ICall extends Instruction {
    constructor(targetLabel: string, nargs: number);
    get targetLabel(): string;
    get nargs(): number;
}
export declare class IReturn extends Instruction {
    constructor();
}
export declare class IMakeTuple extends Instruction {
    constructor(size: number);
    get size(): number;
}
export declare class IMakeList extends Instruction {
    constructor(size: number);
    get size(): number;
}
export declare class IMakeStructure extends Instruction {
    constructor(typeName: string, constructorName: string, fieldNames: string[]);
    get typeName(): string;
    get constructorName(): string;
    get fieldNames(): string[];
}
export declare class IUpdateStructure extends Instruction {
    constructor(typeName: string, constructorName: string, fieldNames: string[]);
    get typeName(): string;
    get constructorName(): string;
    get fieldNames(): string[];
}
export declare class IReadTupleComponent extends Instruction {
    constructor(index: number);
    get index(): number;
}
export declare class IReadStructureField extends Instruction {
    constructor(fieldName: string);
    get fieldName(): string;
}
export declare class IReadStructureFieldPop extends Instruction {
    constructor(fieldName: string);
    get fieldName(): string;
}
export declare class IAdd extends Instruction {
    constructor();
}
export declare class IDup extends Instruction {
    constructor();
}
export declare class IPop extends Instruction {
    constructor();
}
export declare class IPrimitiveCall extends Instruction {
    constructor(primitiveName: string, nargs: number);
    get primitiveName(): string;
    get nargs(): number;
}
export declare class ISaveState extends Instruction {
    constructor();
}
export declare class IRestoreState extends Instruction {
    constructor();
}
export declare class ITypeCheck extends Instruction {
    constructor(type: Type);
    get type(): Type;
}
//# sourceMappingURL=instruction.d.ts.map