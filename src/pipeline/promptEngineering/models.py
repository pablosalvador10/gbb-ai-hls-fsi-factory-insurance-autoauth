from pydantic import BaseModel, Field
from typing import List, Optional

class PolicyLevelInformation(BaseModel):
    """
    Represents high-level policy inputs (term, effective date, etc.).
    """
    policy_effective_date: str = Field(default="Not provided", alias="policy_effective_date")
    policy_term: str = Field(default="Not provided", alias="policy_term")
    policy_type: str = Field(default="Not provided", alias="policy_type")
    binding_date_time: str = Field(default="Not provided", alias="binding_date_time")
    policy_payment_plan: str = Field(default="Not provided", alias="policy_payment_plan")

    # Signatures / acknowledgments
    applicant_signature: str = Field(default="Not provided", alias="applicant_signature")
    agent_signature: str = Field(default="Not provided", alias="agent_signature")
    um_uim_form: str = Field(default="Not provided", alias="um_uim_form")
    named_driver_exclusion_form: str = Field(default="Not provided", alias="named_driver_exclusion_form")
    misrep_disclosure: str = Field(default="Not provided", alias="misrep_disclosure")


class ApplicantInformation(BaseModel):
    """
    Represents the primary applicant's details.
    """
    applicant_name: str = Field(default="Not provided", alias="applicant_name")
    applicant_dob: str = Field(default="Not provided", alias="applicant_dob")
    applicant_id: str = Field(default="Not provided", alias="applicant_id")
    applicant_address: str = Field(default="Not provided", alias="applicant_address")
    applicant_mailing_address: str = Field(default="Not provided", alias="applicant_mailing_address")
    applicant_phone: str = Field(default="Not provided", alias="applicant_phone")
    applicant_email: str = Field(default="Not provided", alias="applicant_email")
    applicant_ssn: str = Field(default="Not provided", alias="applicant_ssn")
    applicant_marital_status: str = Field(default="Not provided", alias="applicant_marital_status")
    applicant_military_status: str = Field(default="Not provided", alias="applicant_military_status")
    applicant_homeowner_status: str = Field(default="Not provided", alias="applicant_homeowner_status")


class DriverDetail(BaseModel):
    """
    Represents a single driver's details.
    """
    driver_name: str = Field(default="Not provided", alias="driver_name")
    driver_dob: str = Field(default="Not provided", alias="driver_dob")
    driver_relationship: str = Field(default="Not provided", alias="driver_relationship")
    driver_license_state: str = Field(default="Not provided", alias="driver_license_state")
    driver_license_number: str = Field(default="Not provided", alias="driver_license_number")
    driver_license_status: str = Field(default="Not provided", alias="driver_license_status")
    driver_sr22: str = Field(default="Not provided", alias="driver_sr22")  # Yes/No
    driver_accident_violation_history: str = Field(
        default="Not provided", alias="driver_accident_violation_history"
    )
    driver_military_status: str = Field(default="Not provided", alias="driver_military_status")
    driver_excluded: str = Field(default="Not provided", alias="driver_excluded")  # Yes/No


class VehicleDetail(BaseModel):
    """
    Represents a single vehicle's details.
    """
    vehicle_year: str = Field(default="Not provided", alias="vehicle_year")
    vehicle_make: str = Field(default="Not provided", alias="vehicle_make")
    vehicle_model: str = Field(default="Not provided", alias="vehicle_model")
    vehicle_vin: str = Field(default="Not provided", alias="vehicle_vin")
    vehicle_ownership: str = Field(default="Not provided", alias="vehicle_ownership")
    vehicle_garaging_address: str = Field(
        default="Not provided", alias="vehicle_garaging_address"
    )
    vehicle_usage: str = Field(default="Not provided", alias="vehicle_usage")
    vehicle_existing_damage: str = Field(default="Not provided", alias="vehicle_existing_damage")
    vehicle_age: str = Field(default="Not provided", alias="vehicle_age")
    vehicle_modifications: str = Field(default="Not provided", alias="vehicle_modifications")
    vehicle_salvage_title: str = Field(default="Not provided", alias="vehicle_salvage_title")
    vehicle_months_in_ohio: str = Field(default="Not provided", alias="vehicle_months_in_ohio")
    vehicle_class: str = Field(default="Not provided", alias="vehicle_class")
    vehicle_prohibited_make: str = Field(default="Not provided", alias="vehicle_prohibited_make")


class CoverageSelections(BaseModel):
    """
    Represents coverage selection details.
    """
    coverage_liability_limits: str = Field(default="Not provided", alias="coverage_liability_limits")
    coverage_um_uim: str = Field(default="Not provided", alias="coverage_um_uim")
    coverage_comp_deductible: str = Field(default="Not provided", alias="coverage_comp_deductible")
    coverage_collision_deductible: str = Field(
        default="Not provided", alias="coverage_collision_deductible"
    )
    coverage_comp_collision_eligible: str = Field(
        default="Not provided", alias="coverage_comp_collision_eligible"
    )
    coverage_um_pd: str = Field(default="Not provided", alias="coverage_um_pd")
    coverage_med_pay: str = Field(default="Not provided", alias="coverage_med_pay")
    coverage_rental: str = Field(default="Not provided", alias="coverage_rental")
    coverage_towing: str = Field(default="Not provided", alias="coverage_towing")
    coverage_custom_equip: str = Field(default="Not provided", alias="coverage_custom_equip")


class DiscountInformation(BaseModel):
    """
    Represents all discount-related fields.
    """
    discount_prior_insurance: str = Field(default="Not provided", alias="discount_prior_insurance")
    discount_homeowner_proof: str = Field(default="Not provided", alias="discount_homeowner_proof")
    discount_military_proof: str = Field(default="Not provided", alias="discount_military_proof")
    discount_senior_defensive_driver: str = Field(
        default="Not provided", alias="discount_senior_defensive_driver"
    )
    discount_auto_pay: str = Field(default="Not provided", alias="discount_auto_pay")
    discount_paid_in_full: str = Field(default="Not provided", alias="discount_paid_in_full")
    discount_advance_purchase: str = Field(
        default="Not provided", alias="discount_advance_purchase"
    )


class SurchargeInformation(BaseModel):
    """
    Represents all surcharge-related fields.
    """
    surcharge_license_status: str = Field(default="Not provided", alias="surcharge_license_status")
    surcharge_at_fault_accidents: str = Field(
        default="Not provided", alias="surcharge_at_fault_accidents"
    )
    surcharge_major_violations: str = Field(
        default="Not provided", alias="surcharge_major_violations"
    )
    surcharge_sr22: str = Field(default="Not provided", alias="surcharge_sr22")
    surcharge_policy_activity: str = Field(default="Not provided", alias="surcharge_policy_activity")
    surcharge_unacceptable_risk: str = Field(
        default="Not provided", alias="surcharge_unacceptable_risk"
    )

class AutoUnderwritingData(BaseModel):
    """
    Top-level container holding all relevant auto underwriting fields.
    """
    policy_level: PolicyLevelInformation
    applicant_info: ApplicantInformation
    driver_info: List[DriverDetail]
    vehicle_info: List[VehicleDetail]
    coverage_selections: CoverageSelections
    discounts: DiscountInformation
    surcharges: SurchargeInformation
    policy_text: str = Field(default="Not provided", alias="policy_text")