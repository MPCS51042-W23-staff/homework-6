import json
import statistics

def summarize_weather(filename="weather.json"):
    """
    Reads weather data from a JSON file and summarizes it.

    Inputs:
        filename (str): Filename for weather data.

    Returns:
        Dictionary with the following keys:
           start_date:      Date of first entry (string)
           end_date:        Date of last entry (string)
           max_high:        Maximum high temperature in the data (float).
           min_low:         Minimum low temperature in the data (float).
           mean_high:    Computed mean of high temperatures (float).
           mean_low:     Computed mean of low temperatures (float).
           std_dev_high:    Computed standard deviation of high temperatures (float).
           std_dev_low:     Computed standard deviation of low temperatures (float).
    """
    # 1) Open weather.json & read data as a string.
    # 2) Use json.load to transform data from a string to Python objects.
    # 3) Compute & return statistics as shown in docstring.


def main():
    """
    Reads in weather data from weather.json and prints out a summary.
    """
    summary = summarize_weather()
    print("""       Weather Report
===========================
{start_date}       {end_date}
===========================
High Temperature:   {max_high:>6.1f}
     Average:       {mean_high:>6.1f}
     Std. Dev:      {std_dev_high:>6.1f}
Low Temperature:    {min_low:>6.1f}
     Average:       {mean_low:>6.1f}
     Std. Dev:      {std_dev_low:>6.1f}
          """.format(**summary))


if __name__ == "__main__":
    main()
