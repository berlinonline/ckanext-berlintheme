bde_bundle_base = https://www.berlin.de/i9f/r1/bundle/
bde_asset_service_css = ${bde_bundle_base}berlin_assetservice.css
bde_asset_service_js = ${bde_bundle_base}berlin_assetservice.js
bde_fontawesome = ${bde_bundle_base}fontawesome.all.min.css

install_bde: ckanext/berlintheme/theme/assets/css/berlin_assetservice.css ckanext/berlintheme/theme/assets/css/fontawesome.all.min.css ckanext/berlintheme/theme/assets/js/berlin_assetservice.js

ckanext/berlintheme/theme/assets/css/berlin_assetservice.css:
	curl -o $@ "$(bde_asset_service_css)"

ckanext/berlintheme/theme/assets/css/fontawesome.all.min.css:
	curl -o $@ "$(bde_fontawesome)"

ckanext/berlintheme/theme/assets/js/berlin_assetservice.js: ckanext/berlintheme/theme/assets/js
	curl -o $@ "$(bde_asset_service_js)"


ckanext/berlintheme/theme/assets/js:
	mkdir -p $@

clean_bde:
	rm ckanext/berlintheme/theme/assets/js/berlin_assetservice.js
	rm ckanext/berlintheme/theme/assets/css/fontawesome.all.min.css
	rm ckanext/berlintheme/theme/assets/css/berlin_assetservice.css