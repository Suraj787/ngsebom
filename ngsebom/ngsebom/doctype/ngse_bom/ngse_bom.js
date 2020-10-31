// Copyright (c) 2020, FirstERP and contributors
// For license information, please see license.txt

cur_frm.fields_dict['itemid'].get_query = function(doc, cdt, cdn) {
	return {
		filters:{'is_purchase_item':1,'item_group':doc.item_group}
	}
}

//drawing filter based on project
cur_frm.fields_dict['drawing_no'].get_query = function(doc, cdt, cdn) {
	return {
		filters:{'project_no':doc.project}
	}
}
//item group filter
cur_frm.fields_dict['item_group'].get_query = function(doc, cdt, cdn) {
	return {
		filters:{'parent_item_group':'Nandan Buying Items'}
	}
}
//assigned_to 
frappe.ui.form.on("NGSE BOM","refresh",function(frm){
  frappe.db.get_single_value("NGSE BOM Setting","assigned_to").then(value => {
               console.log(value)
             cur_frm.set_value("assigned_to",value)})
})

frappe.ui.form.on('NGSE BOM', {
	onload: function(frm) {
     if(frm.is_dirty()){
       cur_frm.set_value("added_date",frappe.datetime.get_today());
       cur_frm.set_value("required_date",frappe.datetime.add_days(get_today(),3));
     }
	 },
   validate: function(frm){
     cur_frm.set_value("last_edit_date",frappe.datetime.get_today());
   }
});

frappe.ui.form.on('NGSE BOM', "status",function(){
 if (cur_frm.doc.status == 'Kitted'){
    cur_frm.set_value("kitted_date_by",frappe.session.user);
    cur_frm.refresh_fields("kitted_date_by")
    cur_frm.set_value("kitted_date",frappe.datetime.get_today());
        }
    }
);
frappe.ui.form.on('NGSE BOM', "status",function(){
 if (cur_frm.doc.status == 'Ordered'){
    cur_frm.set_value("ordered_date_by",frappe.session.user);
    cur_frm.refresh_fields("ordered_date_by")
    cur_frm.set_value("ordered_date",frappe.datetime.get_today());
        }
    }
);
frappe.ui.form.on('NGSE BOM', "status",function(){
 if (cur_frm.doc.status == 'Released'){
    cur_frm.set_value("released_date_by",frappe.session.user);
    cur_frm.refresh_fields("released_date_by")
    cur_frm.set_value("released_date",frappe.datetime.get_today());
        }
    }
);



//critcal
frappe.ui.form.on("NGSE BOM", {
        priority: function(frm) {
        if(frm.doc.priority == 'Critical'){
        set_css(frm);
          }
        else{
          document.querySelectorAll("[data-fieldname='priority']")[1].style.backgroundColor ="white";
        }
                        
        }
});

var set_css = function (frm)
    {
   
    document.querySelectorAll("[data-fieldname='priority']")[1].style.backgroundColor ="red";

    }