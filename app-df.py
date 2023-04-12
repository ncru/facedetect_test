from deepface import DeepFace as df

df.stream(
    "db",
    model_name="VGG-Face",
    detector_backend="opencv",
    time_threshold=1,
    frame_threshold=1,
)
