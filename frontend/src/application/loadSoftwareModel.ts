import { SoftwareModelInfo } from "@/domain/model/softwareModel";

export const getSoftwareModelInfo = (): SoftwareModelInfo => ({
  name: "software.glb",
  path: "/models/software.glb",
  scale: [1, 1, 1],
  position: [0, 0, 0],
  rotation: [0, 0, 0],
});
