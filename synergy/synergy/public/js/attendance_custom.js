frappe.ui.form.on('Attendance', {
    refresh(frm) {
        if (frm.fields_dict.status) {
            let options = frm.fields_dict.status.df.options.split('\n');
            if (!options.includes('On Duty')) {  // Capitalize same as in Python
                options.push('On Duty');
                frm.fields_dict.status.df.options = options.join('\n');
            }
            frm.refresh_field('status');
        }
    }
});
