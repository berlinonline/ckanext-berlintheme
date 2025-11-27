// Script to guide users through the 3 checkboxes for editing metadata about
// personal data.
// 
// - If there is no personal data, the other two checkboxes should not be visible
// and have to be unchecked.
// - If there is personal data, the other two checkboxes should be visible and one (and only one)
// of the other two checkboxes has to be checked.

document.addEventListener("DOMContentLoaded", function () {
    const personalDataCheckbox = document.getElementById("field-personal_data");
    const exemptionCheckbox = document.getElementById("field-personal_data_exemption");
    const anonymizedCheckbox = document.getElementById("field-data_anonymized");

    const exemptionGroup = exemptionCheckbox.closest(".form-group");
    const anonGroup = anonymizedCheckbox.closest(".form-group");

    function toggleGroups() {
        if (personalDataCheckbox.checked) {
            exemptionGroup.style.display = "";
            anonGroup.style.display = "";
        } else {
            exemptionGroup.style.display = "none";
            anonGroup.style.display = "none";

            // Reset both when hidden
            exemptionCheckbox.checked = false;
            anonymizedCheckbox.checked = false;
        }
    }

    function enforceRadioBehavior(e) {
        if (!personalDataCheckbox.checked) return; // Only active when visible

        // If user checks one -> uncheck the other
        if (e.target === exemptionCheckbox && exemptionCheckbox.checked) {
            anonymizedCheckbox.checked = false;
        } else if (e.target === anonymizedCheckbox && anonymizedCheckbox.checked) {
            exemptionCheckbox.checked = false;
        }

        // If user unchecks one -> check the other
        if (e.target === exemptionCheckbox && !exemptionCheckbox.checked) {
            anonymizedCheckbox.checked = true;
        } else if (e.target === anonymizedCheckbox && !anonymizedCheckbox.checked) {
            exemptionCheckbox.checked = true;
        }
    }

    // Initialize on page load
    toggleGroups();

    personalDataCheckbox.addEventListener("change", toggleGroups);

    exemptionCheckbox.addEventListener("change", enforceRadioBehavior);
    anonymizedCheckbox.addEventListener("change", enforceRadioBehavior);
});
