/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Component, xml } from "@odoo/owl";

class StarRating extends Component{
    setup(){
        console.log("Star Rating")
    };
    onClick(ev) {
         console.log('Event Clicked');
         const value = $(ev.target).attr('value');
         console.log('evvvvvvvv');
         this._setValue(value);
         console.log('ttrstg');

    }
};

StarRating.template = "device_management.star_template";
registry.category("fields").add("star_rating", StarRating);
