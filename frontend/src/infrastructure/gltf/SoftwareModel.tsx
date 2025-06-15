import { useSoftwareGLTF } from "@/infrastructure/gltf/gltfLoader";
import { JSX } from "react";

type PrimitiveProps = Omit<JSX.IntrinsicElements["primitive"], "object">;

export default function SoftwareModel(props: PrimitiveProps) {
  const gltf = useSoftwareGLTF();
  return <primitive object={gltf.scene} {...props} />;
}
