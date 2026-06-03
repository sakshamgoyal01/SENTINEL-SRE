import { api } from "./axios";

export async function getProcessedTelemetry() {
  const response =
    await api.get(
      "/processed-telemetry/"
    );

  return response.data;
}
