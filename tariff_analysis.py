def calculate_flat_rate_bill(consumption, rate, fixed_fee):
    """
    Calculates the total electricity bill provided a flat-rate tariff.

    @param - consumption: float, electricity consumption (kWh)
             rate: float, cost per kWh of electricity
             fixed_fee: float, fixed monthly fee

    @return: float, total electricity bill
    """

    if consumption < 0:
        raise ValueError("Electricity consumption cannot be negative.")

    if rate < 0:
        raise ValueError("Cost per kWh cannot be negative.")

    if fixed_fee < 0:
        raise ValueError("Fixed monthly fee cannot be negative.")

    return (consumption * rate) + fixed_fee


def calculate_tiered_bill(consumption, tiers, fixed_fee):
    """
    Calculates the total electricity bill provided differing unit prices depending on the total consumption volume (tiered tariffs)

    @param - consumption: float, electricity consumption (kWh)
             tiers: list, list of Tuples containing (maximum kWh for tier, cost per kWh of electricity)
             fixed_fee: float, fixed monthly fee
             
    @return: float, total electricity bill
    """

    if consumption < 0:
        raise ValueError("Electricity consumption cannot be negative.")

    if fixed_fee < 0:
        raise ValueError("Fixed monthly fee cannot be negative.")

    if not tiers:
        raise ValueError("At least one tariff tier is required.")

    total = fixed_fee
    previous_limit = 0
    remaining_consum = consumption

    # Iterate through the tiers
    for limit, rate in tiers:
        if limit <= previous_limit:
            raise ValueError("Tier limits must be increasing.")

        if rate < 0:
            raise ValueError("Tariff rate cannot be negative.")

        tier_usage = min(remaining_consum, limit - previous_limit)

        # Update variables each loop
        total += tier_usage * rate
        remaining_consum -= tier_usage
        previous_limit = limit

        if remaining_consum <= 0:
            break

    # If consumption exceeds the final tier
    if remaining_consum > 0:
        final_rate = tiers[-1][1]
        total += remaining_consum * final_rate

    return total


def calculate_saving_suggestion(current_cost, alternative_cost):
    """
    Calculates the money saved on electricital bills between two differing tariffs

    @param - current_cost: float, cost of electricity under the current tariff
             alternative_cost: float, cost of electricity under an alternative tariff
             
    @return: float, amount of money saved (or 0 if alternative cost is equal or more)
    """

    if current_cost < 0:
        raise ValueError("The current cost of electricity cannot be negative.")

    if alternative_cost < 0:
        raise ValueError("The alternative cost of electricity cannot be negative.")

    # If current tariff is more expensive, subtract alternative tariff. Otherwise, return 0
    if alternative_cost < current_cost:
        return current_cost - alternative_cost
    else:
        return 0.0