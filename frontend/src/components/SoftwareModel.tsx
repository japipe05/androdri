"use client";
import { useGLTF } from "@react-three/drei";
import { JSX } from "react";

type PrimitiveProps = Omit<JSX.IntrinsicElements["primitive"], "object">;

export default function SoftwareModel(props: PrimitiveProps) {
  const gltf = useGLTF("/models/software.glb");
  return <primitive object={gltf.scene} {...props} />;
}
