import { APIJBoard } from './board_formats';
export declare class GobstonesInterpreterAPI {
    config: {
        setLanguage: (code: string) => void;
        setInfiniteLoopTimeout: (milliseconds: number) => void;
        setXGobstonesEnabled: (isEnabled: boolean) => void;
    };
    gbb: {
        read: (gbb: string) => APIJBoard;
        write: (apiboard: APIJBoard) => string;
    };
    getAst: (sourceCode: string) => any;
    parse: (sourceCode: string) => any;
    _withState: (sourceCode: string, useLinter: boolean, action: Function) => any;
    constructor();
}
//# sourceMappingURL=api.d.ts.map