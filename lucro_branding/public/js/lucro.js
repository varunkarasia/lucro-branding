/* Lucro branding: runtime overrides for values Frappe hardcodes in JS. */

(function apply() {
  if (window.frappe && frappe.utils && frappe.utils.desktop_pallete) {
    // Desk/workspace tiles are painted inline from this palette.
    frappe.utils.desktop_pallete.blue = "#00444e";
    frappe.utils.desktop_pallete.gray = "#5b6b6e";
  } else {
    setTimeout(apply, 50);
  }
})();
