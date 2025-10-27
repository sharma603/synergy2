import frappe
from hrms.hr.doctype.attendance.attendance import Attendance


class CustomAttendance(Attendance):
    def validate(self):
        
        self.validate_attendance_date()
        self.validate_duplicate_record()
        self.validate_employee_status()
       

        # Now run our custom status validation
        valid_statuses = ["Present", "Absent", "On Leave", "Half Day", "Work From Home","OD" ,"On Duty"]

        if self.status not in valid_statuses:
            frappe.throw(f"Invalid status '{self.status}'. Must be one of {', '.join(valid_statuses)}")

    # def mark_attendance(self):
    #     """
    #     Allow marking attendance with  (On Duty) status.
    #     """
    #     if self.status == "On Duty":
    #         self.db_set("status", "On Duty")
    #         frappe.msgprint(f"Attendance marked as On Duty for {self.employee}")
    #     else:
    #         super().mark_attendance()
