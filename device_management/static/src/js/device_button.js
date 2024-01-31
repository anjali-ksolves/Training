/** @odoo-module **/

import { ConfirmationDialog } from "@web/core/confirmation_dialog/confirmation_dialog";
import { patch } from "@web/core/utils/patch";
import { ListController } from "@web/views/list/list_controller";
import { Dialog } from "@web/core/dialog/dialog";
import core from 'web.core';
import { _t } from "@web/core/l10n/translation";
import { sprintf } from "@web/core/utils/strings";

patch(ListController.prototype, 'device_button', {

   _onTestClick() {
        console.log("Hellohiee");
        this.dialogService.add(ConfirmationDialog, {
            title: "Model",
            body: sprintf(_t("Model: %s"), this.props.resModel),
        });
   },

});