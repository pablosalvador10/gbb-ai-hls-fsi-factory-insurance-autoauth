from typing import List, Optional
from pydantic import BaseModel, Field
import os
from jinja2 import Environment, FileSystemLoader
from src.pipeline.promptEngineering.models import AutoUnderwritingData

class PromptManager:
    def __init__(self, template_dir: str = "templates"):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        template_path = os.path.join(current_dir, template_dir)
        self.env = Environment(
            loader=FileSystemLoader(searchpath=template_path),
            autoescape=False
        )

        # Example: log which templates are found
        found_templates = self.env.list_templates()
        print(f"Templates in {template_path}: {found_templates}")

    def get_prompt(self, template_name: str, **kwargs) -> str:
        try:
            template = self.env.get_template(template_name)
            return template.render(**kwargs)
        except Exception as e:
            raise ValueError(f"Error rendering template '{template_name}': {e}")

    def create_prompt_auto_system_underwriting(self, query: str) -> str:
        return self.get_prompt("underwriting_o1_system_prompt.jinja", query=query)

    def create_prompt_auto_user_underwriting(
        self,
        auto_data: AutoUnderwritingData
    ) -> str:
        """
        Renders an auto-insurance underwriting prompt using the new Pydantic classes.
        Requires a template named 'auto_underwriting_user_prompt.jinja' in your template_dir.
        """
        template_name = "underwriting_o1_user_prompt.jinja"
        
        return self.get_prompt(
            template_name,
            # Policy Level
            policy_effective_date=auto_data.policy_level.policy_effective_date,
            policy_term=auto_data.policy_level.policy_term,
            policy_type=auto_data.policy_level.policy_type,
            binding_date_time=auto_data.policy_level.binding_date_time,
            policy_payment_plan=auto_data.policy_level.policy_payment_plan,
            applicant_signature=auto_data.policy_level.applicant_signature,
            agent_signature=auto_data.policy_level.agent_signature,
            um_uim_form=auto_data.policy_level.um_uim_form,
            named_driver_exclusion_form=auto_data.policy_level.named_driver_exclusion_form,
            misrep_disclosure=auto_data.policy_level.misrep_disclosure,
            
            # Applicant Info
            applicant_name=auto_data.applicant_info.applicant_name,
            applicant_dob=auto_data.applicant_info.applicant_dob,
            applicant_id=auto_data.applicant_info.applicant_id,
            applicant_address=auto_data.applicant_info.applicant_address,
            applicant_mailing_address=auto_data.applicant_info.applicant_mailing_address,
            applicant_phone=auto_data.applicant_info.applicant_phone,
            applicant_email=auto_data.applicant_info.applicant_email,
            applicant_ssn=auto_data.applicant_info.applicant_ssn,
            applicant_marital_status=auto_data.applicant_info.applicant_marital_status,
            applicant_military_status=auto_data.applicant_info.applicant_military_status,
            applicant_homeowner_status=auto_data.applicant_info.applicant_homeowner_status,

            # Drivers
            driver_info=auto_data.driver_info,  # This might be a list of DriverDetail
            # Vehicles
            vehicle_info=auto_data.vehicle_info,  # This might be a list of VehicleDetail

            # Coverage Selections
            coverage_liability_limits=auto_data.coverage_selections.coverage_liability_limits,
            coverage_um_uim=auto_data.coverage_selections.coverage_um_uim,
            coverage_comp_deductible=auto_data.coverage_selections.coverage_comp_deductible,
            coverage_collision_deductible=auto_data.coverage_selections.coverage_collision_deductible,
            coverage_comp_collision_eligible=auto_data.coverage_selections.coverage_comp_collision_eligible,
            coverage_um_pd=auto_data.coverage_selections.coverage_um_pd,
            coverage_med_pay=auto_data.coverage_selections.coverage_med_pay,
            coverage_rental=auto_data.coverage_selections.coverage_rental,
            coverage_towing=auto_data.coverage_selections.coverage_towing,
            coverage_custom_equip=auto_data.coverage_selections.coverage_custom_equip,

            # Discounts
            discount_prior_insurance=auto_data.discounts.discount_prior_insurance,
            discount_homeowner_proof=auto_data.discounts.discount_homeowner_proof,
            discount_military_proof=auto_data.discounts.discount_military_proof,
            discount_senior_defensive_driver=auto_data.discounts.discount_senior_defensive_driver,
            discount_auto_pay=auto_data.discounts.discount_auto_pay,
            discount_paid_in_full=auto_data.discounts.discount_paid_in_full,
            discount_advance_purchase=auto_data.discounts.discount_advance_purchase,

            # Surcharges
            surcharge_license_status=auto_data.surcharges.surcharge_license_status,
            surcharge_at_fault_accidents=auto_data.surcharges.surcharge_at_fault_accidents,
            surcharge_major_violations=auto_data.surcharges.surcharge_major_violations,
            surcharge_sr22=auto_data.surcharges.surcharge_sr22,
            surcharge_policy_activity=auto_data.surcharges.surcharge_policy_activity,
            surcharge_unacceptable_risk=auto_data.surcharges.surcharge_unacceptable_risk,

            # Policy Text
            policy_text=auto_data.policy_text
        )
