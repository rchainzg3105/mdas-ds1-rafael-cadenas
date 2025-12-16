import { Document } from "./Document";
import { Extension } from "./enum/Extension";
export class Proposal extends Document {
    public readonly maxFileSize: number = 5
    constructor(
        public readonly name: string,
        public readonly fileSize: number,
        public readonly proposalDate: Date,
        public readonly client: string,
    ){
        super(name, fileSize)
    }

    validateDocument(): boolean {
        return super.validateName() && 
                super.validateExtension(Extension.PDF) &&
                super.validateExtension(Extension.DOCX) &&
                super.validateSize(this.maxFileSize); 
        }
}