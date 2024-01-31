/** @odoo-module **/

import { ListController } from "@web/views/list/list_controller";
import { registry } from '@web/core/registry';
import { listView } from '@web/views/list/list_view';
import { useService } from "@web/core/utils/hooks";

export class ApprovedButton extends ListController {
   setup() {
       this.orm = useService("orm");
       this.notification = useService("notification");
       super.setup();
   }
   onClick() {
         console.log("hiee")
   }
   async getStateApproved() {
      const record_ids = await this.getSelectedResIds();
      await this.orm.call('device.assignment', 'check_rpc', [record_ids]);
      console.log(record_ids);
      if('check_rpc'){
          this.notification.add(this.env._t("Status Updated"), {
               type: "success",
          });
      }

//        this.rpc({
//             model: 'device.assignment',
//             method: 'check_rpc',
//             args: [],
//        });
   }
}
registry.category("views").add("approved", {
        ...listView,
        Controller: ApprovedButton,
        buttonTemplate: "device_management.approved_state",
    });