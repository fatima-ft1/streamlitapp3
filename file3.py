import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def create_animation():
    # Create figure with subplots
    fig = make_subplots(rows=1, cols=2, subplot_titles=("Sine", "Cosine"))

    # Generate data
    x = np.linspace(0, 2 * np.pi, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

    # Create initial traces
    trace1 = go.Scatter(x=x, y=y1, mode="lines", name="Sine")
    trace2 = go.Scatter(x=x, y=y2, mode="lines", name="Cosine")

    # Add traces to the figure
    fig.add_trace(trace1, row=1, col=1)
    fig.add_trace(trace2, row=1, col=2)

    # Set initial frame
    frames = [go.Frame(data=[], layout=fig.layout)]

    # Create frames for animation
    for i in range(len(x)):
        frame_data = [
            go.Frame(data=[
                go.Scatter(x=x[:i+1], y=y1[:i+1]),
                go.Scatter(x=x[:i+1], y=y2[:i+1])
            ])
        ]
        frames.extend(frame_data)

    # Update layout
    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                buttons=[
                    dict(label="Play", method="animate", args=[None, {"frame": {"duration": 50, "redraw": True}, "fromcurrent": True, "transition": {"duration": 0}}]),
                    dict(label="Pause", method="animate", args=[[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate", "transition": {"duration": 0}}])
                ],
            )
        ]
    )

    # Update frames in figure
    fig.frames = frames

    return fig

def main():
    st.title("Animated Visualizations")
    st.write("This app showcases animated visualizations using Plotly.")

    fig = create_animation()

    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
