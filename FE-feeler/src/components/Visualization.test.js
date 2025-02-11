import { render, screen, waitFor } from "@testing-library/react";
import Visualization from "./Visualization";
import { getVisualization } from "../api";
import { BrowserRouter } from "react-router-dom";

// Mock API
jest.mock("../api", () => ({
  getVisualization: jest.fn(),
}));

// Mock Chart.js
jest.mock('react-chartjs-2', () => ({
  Line: function DummyChart() {
    return (
      <div data-testid="line-chart" className="mock-chart">
        Chart Component
      </div>
    );
  }
}));

// Mock alert
window.alert = jest.fn();

describe("Visualization Component", () => {
  test("renders loading state initially", () => {
    render(
      <BrowserRouter>
        <Visualization />
      </BrowserRouter>
    );

    expect(screen.getByText(/Loading.../i)).toBeInTheDocument();
  });

  test("renders graph with fetched data", async () => {
    const mockData = {
      labels: ["2025-01-01", "2025-01-02", "2025-01-03"],
      sentiments: [1, -1, 1],
    };

    getVisualization.mockResolvedValueOnce({ data: mockData });

    render(
      <BrowserRouter>
        <Visualization />
      </BrowserRouter>
    );

    // Wait for loading state to disappear
    await waitFor(() => {
      expect(screen.queryByText(/Loading.../i)).not.toBeInTheDocument();
    });

    // Check if the title is rendered
    expect(screen.getByText(/Past Sentiments/i)).toBeInTheDocument();
    
    // Check if the Line chart component is rendered
    expect(screen.getByTestId('line-chart')).toBeInTheDocument();
  });

  test("renders error state on API failure", async () => {
    getVisualization.mockRejectedValueOnce(new Error("Failed to fetch data"));

    render(
      <BrowserRouter>
        <Visualization />
      </BrowserRouter>
    );

    await waitFor(() => {
      expect(window.alert).toHaveBeenCalledWith("Error fetching visualization data.");
    });
  });
});