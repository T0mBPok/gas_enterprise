<script setup lang="ts">
import { onMounted, ref } from 'vue'
import * as THREE from 'three'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls'
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader'
import api from '@/services/api'

const props = defineProps<{ modelId: number }>()
const container = ref<HTMLDivElement | null>(null)

onMounted(async () => {
  const scene = new THREE.Scene()
  scene.background = new THREE.Color(0xdddddd)

  const camera = new THREE.PerspectiveCamera(
    60,
    container.value!.clientWidth / container.value!.clientHeight,
    0.1,
    10000
  )
  camera.position.set(150, 150, 150)

  const renderer = new THREE.WebGLRenderer({ antialias: true })
  renderer.setSize(container.value!.clientWidth, container.value!.clientHeight)
  container.value!.appendChild(renderer.domElement)

  const controls = new OrbitControls(camera, renderer.domElement)
  controls.enableDamping = true

  scene.add(new THREE.AmbientLight(0xffffff, 0.6))
  const light = new THREE.DirectionalLight(0xffffff, 1)
  light.position.set(10, 10, 10)
  scene.add(light)

  // загружаем glTF через axios
  const res = await api.get(`/models/view/${props.modelId}`, {
    responseType: 'arraybuffer'
  })

  const loader = new GLTFLoader()
  const blob = new Blob([res.data], { type: 'model/gltf+json' })
  const url = URL.createObjectURL(blob)

  loader.load(url, gltf => {
    gltf.scene.traverse((child: any) => {
      if (child.isMesh) {
        child.material.side = THREE.DoubleSide
        child.material.transparent = true
      }
    })
    scene.add(gltf.scene)
  })


  const animate = () => {
    requestAnimationFrame(animate)
    controls.update()
    renderer.render(scene, camera)
  }
  animate()
})
</script>

<template>
  <div ref="container" style="width: 100%; height: 100vh;" />
</template>