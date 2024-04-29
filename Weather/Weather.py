# Design and develop a distributed application to find the coolest/hottest year from the
# available weather data. Use weather data from the Internet and process it using MapReduce


from mrjob.job import MRJob
from mrjob.step import MRStep

class MRWeatherAnalysis(MRJob):

    def mapper(self, _, line):
        parts = line.split(',')
        try:
            year = parts[3]  # Fetching the year
            temp = float(parts[4])
            yield year, temp
        except ValueError:
            pass  # Ignore lines with invalid data

    def reducer_get_max_temp(self, year, temps):
        yield None, (max(temps), year)
        #yield None, (min(temps), year)

    def reducer_find_max_temp_year(self, _, year_temp_pairs):
        yield max(year_temp_pairs)
        #yield min(year_temp_pairs)

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer_get_max_temp),
            MRStep(reducer=self.reducer_find_max_temp_year)
        ]

if __name__ == '__main__':
    MRWeatherAnalysis.run()