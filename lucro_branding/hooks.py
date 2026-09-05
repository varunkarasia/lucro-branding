app_name = "lucro_branding"
app_title = "Lucro Branding"
app_publisher = "Lucro PlasteCycle Private Limited"
app_description = "White-labels ERPNext with Lucro brand (teal/lime, Plus Jakarta Sans)"
app_email = "varunkarasia@lucro.in"
app_license = "mit"

# Shown in the browser tab and as the app identity
app_logo_url = "/assets/lucro_branding/images/lucro-logo.png"

# Injected on every desk + website page.
# Bump ?v= on every CSS change — plain (non-bundle) assets get year-long
# cache headers, so without this browsers keep stale styles indefinitely.
app_include_css = ["/assets/lucro_branding/css/lucro.css?v=3"]
web_include_css = ["/assets/lucro_branding/css/lucro.css?v=3"]

# Login page + navbar branding
website_context = {
    "favicon": "/assets/lucro_branding/images/favicon.png",
    "splash_image": "/assets/lucro_branding/images/lucro-logo.png",
}
