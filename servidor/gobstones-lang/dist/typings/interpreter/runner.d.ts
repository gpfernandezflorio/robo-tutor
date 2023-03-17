import { ASTMain, Input } from '@gobstones/gobstones-parser';
import { SymbolTable } from '@gobstones/gobstones-parser';
import { RuntimePrimitives, RuntimeState } from './runtime';
import { ASTDefProcedure, ASTDefFunction, ASTDefType, ASTConstructorDeclaration } from '@gobstones/gobstones-parser';
import { Code } from './instruction';
import { Value } from './value';
export interface RunnerResult {
    result: Value;
    state: RuntimeState;
}
export declare class Runner {
    private _ast;
    private _primitives;
    private _symtable;
    private _linter;
    private _code;
    private _vm;
    private _result;
    constructor();
    initialize(): void;
    run(input: Input): Value;
    runState(input: Input, initialState: RuntimeState): RunnerResult;
    parse(input: Input): void;
    enableLintCheck(linterCheckId: string, enabled: boolean): void;
    lint(): void;
    compile(): void;
    initializeVirtualMachine(initialState: RuntimeState): void;
    execute(initialState: RuntimeState): void;
    executeWithTimeout(initialState: RuntimeState, millisecs: number): void;
    executeWithTimeoutTakingSnapshots(initialState: RuntimeState, millisecs: number, snapshotCallback: Function): void;
    executeEventWithTimeout(eventValue: Value, millisecs: number): void;
    get abstractSyntaxTree(): ASTMain;
    get primitives(): RuntimePrimitives;
    get symbolTable(): SymbolTable;
    get virtualMachineCode(): Code;
    get result(): Value;
    get globalState(): RuntimeState;
    _setLanguageOption(option: string): void;
    regionStack(): string[];
    _newSymtableWithPrimitives(): SymbolTable;
    _astDefType(type: string): ASTDefType;
    _astDefProcedure(procedureName: string): ASTDefProcedure;
    _astDefFunction(functionName: string): ASTDefFunction;
    _astConstructorDeclaration(type: string, constructor: string): ASTConstructorDeclaration;
}
//# sourceMappingURL=runner.d.ts.map