"use client";
import { Canvas } from "@react-three/fiber";
import { OrbitControls, Stage } from "@react-three/drei";
import { Suspense } from "react";
import SoftwareModel from "./SoftwareModel";

export default function ModelViewer() {
  return (
    <div className="w-full h-[400px] md:h-[500px]">
      <Canvas camera={{ position: [0, 0, 4] }}>
        <ambientLight intensity={1.2} /> {/* ✅ Luz ambiental clara */}
        <directionalLight position={[3, 2, 1]} intensity={1} />
        <Suspense fallback={null}>
          <Stage environment="city" intensity={1} shadows={false}>
            <SoftwareModel />
          </Stage>
        </Suspense>
        <OrbitControls enableZoom={false} />
      </Canvas>
    </div>
  );
}
