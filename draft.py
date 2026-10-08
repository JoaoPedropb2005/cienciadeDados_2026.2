from functions.white_noise import white_noise
import plotly.express as px

time, values = white_noise(seed = 100)

px.line(
    x = time,
    y = values
)