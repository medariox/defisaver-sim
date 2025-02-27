from configparser import ConfigParser

def readConfig(section: str):
    '''
    Read the desired section of the config file and return an array containing
    all of the read parameters as a tuple.

    Params:

    section: str
        the section of the config file to read

    Returns:

    config: tuple

        If brownian simulation section:

        init_portfolio, init_collateralization, repay_from, repay_to, boost_from,
        boost_to, service_fee, gas_price, N_paths, volatility, drift, init_price,
        time_horizon, time_step_size

        If continuous limit optimization:

        underlying_return, time_period, volatility
    '''

    #Import config
    config_object = ConfigParser()
    config_object.read("config.ini")

    if section == "Brownian simulation parameters":

        # Initial value of portfolio in ETH
        init_portfolio = float(config_object.get("Brownian simulation parameters", "INITIAL_PORTFOLIO"))

        # Initial collateralization ratio
        init_collateralization = float(config_object.get("Brownian simulation parameters", "INITIAL_COLLATERALIZATION"))

        # Vault and automation settings
        min_ratio = float(config_object.get("Brownian simulation parameters", "MIN_RATIO"))
        repay_from = float(config_object.get("Brownian simulation parameters", "REPAY_FROM"))
        repay_to = float(config_object.get("Brownian simulation parameters", "REPAY_TO"))
        boost_from = float(config_object.get("Brownian simulation parameters", "BOOST_FROM"))
        boost_to = float(config_object.get("Brownian simulation parameters", "BOOST_TO"))
        service_fee = float(config_object.get("Brownian simulation parameters", "SERVICE_FEE"))
        gas_price = float(config_object.get("Brownian simulation parameters", "GAS_PRICE"))

        # Simulation parameters

        # Number of price paths to average over
        N_paths = int(config_object.get("Brownian simulation parameters", "N_PATHS"))
        # Annualized volatility and drift of each path
        volatility = float(config_object.get("Brownian simulation parameters", "VOLATILITY"))
        drift = float(config_object.get("Brownian simulation parameters", "DRIFT"))
        # Initial price of collateral denominated in debt asset
        init_price = float(config_object.get("Brownian simulation parameters", "INITIAL_PRICE"))
        # Time step size (in years)
        time_horizon = float(config_object.get("Brownian simulation parameters", "TIME_HORIZON"))
        time_step_size = float(config_object.get("Brownian simulation parameters", "TIME_STEP_SIZE"))
        end_price = float(config_object.get("Brownian simulation parameters", "END_PRICE"))

        return init_portfolio, init_collateralization, min_ratio, repay_from, repay_to, boost_from, boost_to, service_fee, gas_price, N_paths, volatility, drift, init_price, time_horizon, time_step_size, end_price

    elif section == "Continuous limit optimization parameters":

        underlying_return = float(config_object.get("Continuous limit optimization parameters", "UNDERLYING_RETURN"))
        #In units of years
        time_period = float(config_object.get("Continuous limit optimization parameters", "TIME_PERIOD"))
        #In units of volatility
        volatility = float(config_object.get("Continuous limit optimization parameters", "VOLATILITY"))
        borrow_rate = float(config_object.get("Continuous limit optimization parameters", "BORROW_RATE"))

        return underlying_return, time_period, volatility, borrow_rate

    elif section == "Automated vault optimization":

        init_portfolio = float(config_object.get("Automated vault optimization", "INITIAL_PORTFOLIO"))
        min_ratio = float(config_object.get("Automated vault optimization", "MIN_RATIO"))
        service_fee = float(config_object.get("Automated vault optimization", "SERVICE_FEE"))
        gas_price = float(config_object.get("Automated vault optimization", "GAS_PRICE"))
        volatility = float(config_object.get("Automated vault optimization", "VOLATILITY"))
        start_price = float(config_object.get("Automated vault optimization", "START_PRICE"))
        end_price = float(config_object.get("Automated vault optimization", "END_PRICE"))
        time_horizon = float(config_object.get("Automated vault optimization", "TIME_HORIZON"))
        borrow_rate = float(config_object.get("Continuous limit optimization parameters", "BORROW_RATE"))

        return init_portfolio, min_ratio, service_fee, gas_price, volatility, start_price, end_price, time_horizon, borrow_rate
