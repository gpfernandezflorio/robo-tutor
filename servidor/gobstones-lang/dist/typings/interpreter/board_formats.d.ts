export interface JBoard {
    width: number;
    height: number;
    head: number[];
    board: {
        a: number;
        n: number;
        r: number;
        v: number;
    }[][];
}
export interface Cell {
    blue?: number;
    black?: number;
    red?: number;
    green?: number;
}
export interface APIJBoard {
    width: number;
    height: number;
    head: {
        x: number;
        y: number;
    };
    table: Cell[][];
}
export declare function apiboardFromJboard(jboard: JBoard): APIJBoard;
export declare function apiboardToJboard(apiboard: APIJBoard): JBoard;
export interface GSBoard {
    sizeX: number;
    sizeY: number;
    x: number;
    y: number;
    table: Cell[][];
}
export declare function gbbFromJboard(jboard: JBoard): string;
export declare function gbbToJboard(gbb: string): JBoard;
export declare const DEFAULT_FORMAT = "gs-weblang-cli-json-board";
export declare const BOARD_FORMATS: {};
export declare function readJboardFromFile(filename: string): JBoard;
export declare function writeJboardToFile(filename: string, jboard: JBoard): void;
//# sourceMappingURL=board_formats.d.ts.map