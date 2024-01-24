/** @odoo-module **/

import { registry } from "@web/core/registry";
import { EmailField } from "@web/views/fields/email/email_field";

class ValidEmailField extends EmailField {
   setup(){
       super.setup()
       console.log("Email Field Inheritance")
       console.log(this.props)
   }
   get isValidEmail(){
        let re = /\$+@\$+\.\$+/;
        return re.test(this.props.value)
   }
}
ValidEmailField.template = "school_management.ValidEmailField"
ValidEmailField.supportedTypes = ["char"]

registry.category("fields").add("valid_email", ValidEmailField)