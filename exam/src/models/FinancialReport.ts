import { Document } from "./Document";
import { Extension } from "./enum/Extension";

export class FinancialReport extends Document {
    public readonly maxFileSize: number = 4
    constructor(
        public readonly name: string,
        public readonly fileSize: number,
        public readonly fiscalYear: number,
        public readonly department: string,
    ){
        super(name, fileSize)
    }

        validateDocument(): boolean {
            return super.validateName() && 
                    super.validateExtension(Extension.XLS) &&
                    super.validateExtension(Extension.XLSX) &&
                    super.validateSize(this.maxFileSize); 
        }
}