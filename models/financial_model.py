# AQLA-Financial-Model: Calculating Negative Green Premium
def calculate_aqla_profitability(tons_processed):
    # Costs
    opex_energy_iot = 15.0  # $ per ton
    logistics = 10.0        # $ per ton
    
    # Revenue/Value
    humus_value = 45.0      # $ per ton (Market value of high-grade fertilizer)
    carbon_credit = 25.0    # $ per ton (Based on avoided methane/sequestration)
    health_cost_save = 12.5 # $ per ton (Estimated medical cost reduction)

    unit_profit = (humus_value + carbon_credit + health_cost_save) - (opex_energy_iot + logistics)
    
    # Negative Green Premium is achieved if unit_profit > 0
    return unit_profit * tons_processed

print(f"Projected Profit per Ton: ${calculate_aqla_profitability(1)}")
