import soccerdata as sd

class SoccerService:

    @staticmethod
    def get_available_leagues():
        try:
            return sd.ESPN.available_leagues()
        except Exception as e:
            print(f"Error al obtener ligas: {e}")
            return []

    @staticmethod
    def get_espn_standings(league_id, season):
        try:
            espn = sd.ESPN(leagues=league_id, seasons=season)
            df = espn.read_standings()
            return df.reset_index().to_dict(orient='records')
        except Exception as e:
            print(f"Error when getting standings: {e}")
            return []

    @staticmethod
    def get_schedule(league_id, season):
        try:
            espn = sd.ESPN(leagues=league_id, seasons=season)
            df = espn.read_schedule()

            return df.reset_index().to_dict(orient='records')
        except Exception as e:
            print(f"Error when getting schedule: {e}")
            return []