import { Code, Instruction } from './instruction';
import { Value, Type } from './value';
import { RuntimeState } from './runtime';
export declare class Frame {
    private _routineName;
    private _instructionPointer;
    private _variableTypes;
    private _variables;
    private _stack;
    private _uniqueFrameId;
    constructor(frameId: number, routineName: string, instructionPointer: number);
    get routineName(): string;
    get uniqueFrameId(): number;
    get instructionPointer(): number;
    set instructionPointer(value: number);
    setVariable(name: string, type: Type, value: Value): void;
    unsetVariable(name: string): void;
    getVariableType(name: string): Type;
    getVariable(name: string): Value;
    stackEmpty(): boolean;
    pushValue(value: Value): void;
    stackTop(): Value;
    popValue(): Value;
}
export declare class VirtualMachine {
    private _code;
    private _labelTargets;
    private _nextFrameId;
    private _callStack;
    private _globalStateStack;
    private _primitives;
    private _snapshotCallback?;
    constructor(code: Code, initialState: RuntimeState);
    run(): Value;
    runWithTimeout(millisecs: number): Value;
    runEventWithTimeout(eventValue: Value, millisecs: number): Value;
    runWithTimeoutTakingSnapshots(millisecs: number, snapshotCallback: Function): Value;
    _newFrame(routineName: string, instructionPointer: number): Frame;
    _timeoutIfNeeded(startTime: number, millisecs: number): void;
    _takeSnapshot(routineName: string): void;
    globalState(): RuntimeState;
    setGlobalState(globalState: RuntimeState): void;
    _currentFrame(): Frame;
    _currentInstruction(): Instruction;
    _step(): void;
    _stepPushInteger(): void;
    _stepPushString(): void;
    _stepPushVariable(): void;
    _stepSetVariable(): void;
    _stepUnsetVariable(): void;
    _stepLabel(): void;
    _stepJump(): void;
    _stepJumpIfFalse(): void;
    _stepJumpIfStructure(): void;
    _stepJumpIfTuple(): void;
    _stepCall(): void;
    _stepReturn(): void;
    _stepMakeTuple(): void;
    _stepMakeList(): void;
    _stepMakeStructure(): void;
    _stepUpdateStructure(): void;
    _stepReadTupleComponent(): void;
    _stepReadStructureFieldGeneric(shouldPopStructure: boolean): void;
    _stepReadStructureField(): void;
    _stepReadStructureFieldPop(): void;
    _stepAdd(): void;
    _stepDup(): void;
    _stepPop(): void;
    _stepPrimitiveCall(): void;
    _stepSaveState(): void;
    _stepRestoreState(): void;
    _stepTypeCheck(): void;
    regionStack(): string[];
}
//# sourceMappingURL=vm.d.ts.map