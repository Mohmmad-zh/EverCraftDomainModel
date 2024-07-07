class Alignment:
    GOOD = 'Good'
    EVIL = 'Evil'
    NEUTRAL = 'Neutral'

    @staticmethod
    def is_valid(alignment):
        return alignment in [Alignment.GOOD, Alignment.EVIL, Alignment.NEUTRAL]
