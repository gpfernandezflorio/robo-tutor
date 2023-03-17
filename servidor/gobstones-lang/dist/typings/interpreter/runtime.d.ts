import { ValueInteger, ValueStructure, Type } from './value';
import { SourceReader } from '@gobstones/gobstones-parser';
import { JBoard } from './board_formats';
export declare class RuntimeState {
    private _width;
    private _height;
    private _board;
    private _head;
    constructor();
    clone(): RuntimeState;
    dump(): JBoard;
    load(jboard: JBoard): void;
    putStone(colorName: string): void;
    removeStone(colorName: string): void;
    numStones(colorName: string): ValueInteger;
    move(dirName: string): void;
    goToEdge(dirName: string): void;
    emptyBoardContents(): void;
    canMove(dirName: string): boolean;
    _deltaForDirection(dirName: string): number[];
    _emptyCell(): Record<string, ValueInteger>;
}
declare class PrimitiveOperation {
    private _argumentTypes;
    private _argumentValidator;
    private _implementation;
    constructor(argumentTypes: Type[], argumentValidator: any, implementation: any);
    get argumentTypes(): Type[];
    nargs(): number;
    call(globalState: RuntimeState, args: any[]): any;
    validateArguments(startPos: SourceReader, endPos: SourceReader, globalState: RuntimeState, args: any[]): void;
}
export declare const boolFromValue: (value: ValueStructure) => boolean;
export declare const typesWithOpposite: () => Type[];
export declare const typesWithOrder: () => Type[];
export declare class RuntimePrimitives {
    private _primitiveTypes;
    private _primitiveProcedures;
    private _primitiveFunctions;
    constructor();
    types(): string[];
    typeConstructors(typeName: string): string[];
    constructorFields(typeName: string, constructorName: string): string[];
    isOperation(primitiveName: string): boolean;
    getOperation(primitiveName: string): PrimitiveOperation;
    procedures(): string[];
    isProcedure(primitiveName: string): boolean;
    functions(): string[];
    isFunction(primitiveName: string): boolean;
}
export {};
//# sourceMappingURL=runtime.d.ts.map