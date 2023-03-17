/**
 * This module defines an internal locale definition that any translation
 * should comply to.
 *
 * Note that this module does not provide localization for the Gobstones Language
 * but for this tool internally, and should not be confused with other classes
 * exposed by this package. If you want to learn about how to translate the
 * Gobstones Language see [[models/GobstonesTranslator | the GobstonesTranslator module]] and
 * the [[models/LocaleDefinition | the LocaleDefinition module]].
 *
 * @author Alan Rodas Bonjour <alanrodas@gmail.com>
 *
 * @packageDocumentation
 */
/**
 * Locale is an interface that states the shape a translation for this tool
 * should comply with. Elements of translation object that comply to this
 * interface can be accessed using the elements in the Translator module from
 * the @gobstones/gobstones-core package.
 */
export interface Locale {
    cli: {
        descriptions: {
            tool: string;
            version: string;
            help: string;
            language: string;
            in: string;
            out: string;
        };
        errors: {
            language: string;
            file: string;
        };
    };
}
//# sourceMappingURL=Locale.d.ts.map