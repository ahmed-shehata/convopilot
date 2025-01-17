from convopilot.interface import AudioRecorder, AudioTranscriber, InsightGenerator


class ModuleFactory:
    _recorders = {}
    _transcribers = {}
    _insight_generators = {}

    @classmethod
    def register_recorder(cls, key, recorder):
        if not issubclass(recorder, AudioRecorder):
            raise ValueError("Not an AudioRecorder!")
        cls._recorders[key] = recorder

    @classmethod
    def register_transcriber(cls, key, transcriber):
        if not issubclass(transcriber, AudioTranscriber):
            raise ValueError("Not an AudioTranscriber!")
        cls._transcribers[key] = transcriber

    @classmethod
    def register_insight_generator(cls, key, generator):
        if not issubclass(generator, InsightGenerator):
            raise ValueError("Not an InsightGenerator!")
        cls._insight_generators[key] = generator

    @classmethod
    def create_recorder(cls, key, **kwargs):
        return cls._recorders[key](**kwargs)

    @classmethod
    def create_transcriber(cls, key, **kwargs):
        return cls._transcribers[key](**kwargs)

    @classmethod
    def create_insight_generator(cls, key, **kwargs):
        return cls._insight_generators[key](**kwargs)
