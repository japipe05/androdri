import { useGLTF } from "@react-three/drei";
import { getSoftwareModelInfo } from "@/application/loadSoftwareModel";

export function useSoftwareGLTF() {
  const model = getSoftwareModelInfo();
  return useGLTF(model.path);
}
