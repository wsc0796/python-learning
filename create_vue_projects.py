"""Create runnable Vue3 projects from experiment docs."""
import os

BASE = "C:/Users/50469/python-learning/vue-projects"

# ═══════════════════════════════════════════════════════════════════════
# Project 1: vue3-todo-app (实验七)
# ═══════════════════════════════════════════════════════════════════════

TODO_FILES = {}

TODO_FILES["vue3-todo-app/package.json"] = """{
  "name": "vue3-todo-app",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "vue": "^3.4.0"
  },
  "devDependencies": {
    "@vitejs/plugin-vue": "^5.0.0",
    "vite": "^5.0.0"
  }
}
"""

TODO_FILES["vue3-todo-app/index.html"] = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vue3 待办事项应用</title>
</head>
<body>
  <div id="app"></div>
  <script type="module" src="/src/main.js"></script>
</body>
</html>
"""

TODO_FILES["vue3-todo-app/vite.config.js"] = """import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    port: 8007,
    open: true,
    host: '0.0.0.0',
  },
  resolve: {
    alias: {
      '@': '/src'
    }
  }
})
"""

TODO_FILES["vue3-todo-app/src/main.js"] = """import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')
"""

TODO_FILES["vue3-todo-app/src/App.vue"] = """<template>
  <div class="app-container">
    <TodoHeader />
    <TodoList />
    <TodoFooter />
  </div>
</template>

<script setup>
import { reactive, provide, watch } from 'vue'
import TodoHeader from '@/components/TodoHeader.vue'
import TodoList from '@/components/TodoList.vue'
import TodoFooter from '@/components/TodoFooter.vue'

// 1. 定义响应式待办列表（初始数据）
const todoList = reactive([
  { id: 1, text: '学习第1章 HTML 基础', done: false }
])

// 2. 核心方法定义
const addTodo = (text) => {
  if (!text.trim()) {
    alert('待办内容不能为空！')
    return
  }
  const newTodo = {
    id: Date.now(),
    text: text.trim(),
    done: false
  }
  todoList.push(newTodo)
}

const deleteTodo = (id) => {
  if (window.confirm('确定要删除该待办吗？')) {
    const index = todoList.findIndex(todo => todo.id === id)
    if (index !== -1) {
      todoList.splice(index, 1)
    }
  }
}

const updateTodo = (id, newText) => {
  if (!newText.trim()) {
    alert('修改内容不能为空！')
    return
  }
  const todo = todoList.find(todo => todo.id === id)
  if (todo) {
    todo.text = newText.trim()
  }
}

const toggleDone = (id) => {
  const todo = todoList.find(todo => todo.id === id)
  if (todo) {
    todo.done = !todo.done
  }
}

// 3. 向子组件提供数据和方法
provide('todoList', todoList)
provide('addTodo', addTodo)
provide('deleteTodo', deleteTodo)
provide('updateTodo', updateTodo)
provide('toggleDone', toggleDone)

// 4. 本地存储
const loadTodos = () => {
  const savedTodos = localStorage.getItem('vue3-todo-list')
  if (savedTodos) {
    todoList.splice(0, todoList.length, ...JSON.parse(savedTodos))
  }
}
const saveTodos = () => {
  localStorage.setItem('vue3-todo-list', JSON.stringify(todoList))
}
loadTodos()
watch(todoList, saveTodos, { deep: true })
</script>

<style scoped>
* {
  margin: 0 auto;
  padding: 0;
}
.app-container {
  max-width: 600px;
  width: 90%;
  margin: 0 auto;
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  min-height: 60vh;
  margin-top: 20px;
}

/* 响应式断点：移动端（≤768px） */
@media (max-width: 768px) {
  .app-container {
    padding: 15px;
    margin-top: 10px;
    min-height: 70vh;
  }
}

/* 超小屏（≤480px） */
@media (max-width: 480px) {
  .app-container {
    width: 95%;
    padding: 10px;
    border-radius: 4px;
    box-shadow: none;
    background-color: #fff;
  }
}
</style>
"""

TODO_FILES["vue3-todo-app/src/components/TodoHeader.vue"] = """<template>
  <div class="todo-header">
    <input
      type="text"
      v-model="inputValue"
      placeholder="请输入待办事项..."
      @keyup.enter="handleAdd"
    >
    <button @click="handleAdd">添加待办</button>
  </div>
</template>

<script setup>
import { ref, inject } from 'vue'

const addTodo = inject('addTodo')
const inputValue = ref('')

const handleAdd = () => {
  addTodo(inputValue.value)
  inputValue.value = ''
}
</script>

<style scoped>
.todo-header {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
  width: 100%;
}

input {
  flex: 1;
  padding: 12px 15px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
  box-sizing: border-box;
}

button {
  padding: 12px 20px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  white-space: nowrap;
}

button:hover {
  background-color: #359469;
}

/* 移动端适配 */
@media (max-width: 768px) {
  .todo-header {
    gap: 8px;
    margin-bottom: 15px;
  }
  input {
    padding: 10px 12px;
    font-size: 15px;
  }
  button {
    padding: 10px 15px;
    font-size: 15px;
  }
}

/* 超小屏适配 */
@media (max-width: 480px) {
  .todo-header {
    flex-direction: column;
    gap: 8px;
  }
  button {
    width: 100%;
    padding: 10px 0;
  }
}
</style>
"""

TODO_FILES["vue3-todo-app/src/components/TodoItem.vue"] = """<template>
  <div class="todo-item" :class="{ done: todo.done }">
    <span v-if="!isEditing" class="todo-text">{{ todo.text }}</span>
    <input
      v-else
      type="text"
      v-model="editText"
      @keyup.enter="confirmEdit"
      @blur="confirmEdit"
      ref="editInput"
      class="edit-input"
    >

    <div class="btn-group">
      <button @click="toggleDone(todo.id)" class="btn-toggle">
        {{ todo.done ? '取消' : '完成' }}
      </button>
      <button @click="startEdit" v-if="!isEditing && !todo.done" class="btn-edit">修改</button>
      <button @click="deleteTodo(todo.id)" class="btn-delete">删除</button>
    </div>
  </div>
</template>

<script setup>
import { ref, inject, watch, onMounted } from 'vue'

const props = defineProps({
  todo: {
    type: Object,
    required: true,
    default: () => ({ id: '', text: '', done: false })
  }
})

const deleteTodo = inject('deleteTodo')
const updateTodo = inject('updateTodo')
const toggleDone = inject('toggleDone')

const isEditing = ref(false)
const editText = ref('')
const editInput = ref(null)

const startEdit = () => {
  isEditing.value = true
  editText.value = props.todo.text
}

const confirmEdit = () => {
  updateTodo(props.todo.id, editText.value)
  isEditing.value = false
}

onMounted(() => {
  watch(isEditing, (newVal) => {
    if (newVal && editInput.value) {
      editInput.value.focus()
    }
  })
})
</script>

<style scoped>
.todo-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 10px;
  border-bottom: 1px solid #eee;
  margin-bottom: 8px;
  flex-wrap: wrap;
  gap: 10px;
}

.todo-text {
  flex: 1;
  font-size: 16px;
  word-break: break-all;
}

.done {
  color: #999;
  text-decoration: line-through;
}

.btn-group {
  display: flex;
  gap: 6px;
}

.btn-group button {
  padding: 6px 10px;
  font-size: 14px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  min-width: 60px;
}

.btn-toggle {
  background-color: #2196f3;
  color: white;
}

.btn-edit {
  background-color: #ff9800;
  color: white;
}

.btn-delete {
  background-color: #f44336;
  color: white;
}

.edit-input {
  flex: 1;
  padding: 6px;
  font-size: 16px;
  width: 100%;
  box-sizing: border-box;
}

/* 移动端适配 */
@media (max-width: 768px) {
  .todo-item { padding: 10px 8px; }
  .todo-text { font-size: 15px; }
  .btn-group button { padding: 5px 8px; font-size: 13px; min-width: 50px; }
}

/* 超小屏适配 */
@media (max-width: 480px) {
  .todo-item {
    flex-direction: column;
    align-items: flex-start;
    padding: 10px 0;
  }
  .btn-group {
    width: 100%;
    justify-content: flex-end;
    margin-top: 5px;
  }
  .todo-text { width: 100%; }
}
</style>
"""

TODO_FILES["vue3-todo-app/src/components/TodoList.vue"] = """<template>
  <div class="todo-list">
    <TodoItem
      v-for="todo in todoList"
      :key="todo.id"
      :todo="todo"
    />
    <div class="empty-tip" v-if="todoList.length === 0">
      暂无待办事项，添加你的第一个待办吧！
    </div>
  </div>
</template>

<script setup>
import { inject } from 'vue'
import TodoItem from './TodoItem.vue'

const todoList = inject('todoList')
</script>

<style scoped>
.todo-list {
  padding: 15px;
  background-color: white;
  border-radius: 4px;
  margin-bottom: 20px;
  width: 100%;
  box-sizing: border-box;
}

.empty-tip {
  text-align: center;
  padding: 30px 20px;
  color: #999;
  font-size: 16px;
}

/* 移动端适配 */
@media (max-width: 768px) {
  .todo-list { padding: 10px; margin-bottom: 15px; }
  .empty-tip { padding: 20px 10px; font-size: 15px; }
}

@media (max-width: 480px) {
  .todo-list { padding: 5px 0; background-color: transparent; border-radius: 0; }
}
</style>
"""

TODO_FILES["vue3-todo-app/src/components/TodoFooter.vue"] = """<template>
  <div class="todo-footer">
    <span>待办：{{ pendingCount }} | 已完成：{{ completedCount }}</span>
  </div>
</template>

<script setup>
import { inject, computed } from 'vue'

const todoList = inject('todoList')

const pendingCount = computed(() => {
  return todoList.filter(todo => !todo.done).length
})

const completedCount = computed(() => {
  return todoList.filter(todo => todo.done).length
})
</script>

<style scoped>
.todo-footer {
  padding: 15px 10px;
  text-align: center;
  color: #666;
  font-size: 15px;
  width: 100%;
  box-sizing: border-box;
  position: relative;
}

/* 桌面端固定底部 */
@media (min-width: 992px) {
  .todo-footer {
    position: sticky;
    bottom: 0;
    background-color: #f5f5f5;
    border-radius: 0 0 8px 8px;
    margin: 0 -20px -20px -20px;
    padding: 15px 20px;
  }
}

/* 移动端适配 */
@media (max-width: 768px) {
  .todo-footer { padding: 10px 5px; font-size: 14px; }
}

@media (max-width: 480px) {
  .todo-footer {
    font-size: 13px;
    color: #888;
    border-top: 1px solid #eee;
    margin-top: 10px;
  }
}
</style>
"""

# ═══════════════════════════════════════════════════════════════════════
# Project 2: mall-app (实验八)
# ═══════════════════════════════════════════════════════════════════════

MALL_FILES = {}

MALL_FILES["mall-app/package.json"] = """{
  "name": "mall-app",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "vue": "^3.4.0",
    "vue-router": "^4.3.0",
    "vuex": "^4.1.0",
    "axios": "^1.6.0"
  },
  "devDependencies": {
    "@vitejs/plugin-vue": "^5.0.0",
    "vite": "^5.0.0"
  }
}
"""

MALL_FILES["mall-app/index.html"] = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vue3 响应式商城</title>
</head>
<body>
  <div id="app"></div>
  <script type="module" src="/src/main.js"></script>
</body>
</html>
"""

MALL_FILES["mall-app/vite.config.js"] = """import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    port: 8008,
    open: true,
    host: '0.0.0.0',
    proxy: {
      '/api': {
        target: 'https://portal-api.macrozheng.com',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\\/api/, '')
      }
    }
  },
  resolve: {
    alias: {
      '@': '/src'
    }
  }
})
"""

MALL_FILES["mall-app/src/main.js"] = """import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './assets/css/global.css'
import './assets/css/responsive.css'

const app = createApp(App)
app.use(router)
app.use(store)
app.mount('#app')
"""

MALL_FILES["mall-app/src/App.vue"] = """<template>
  <div class="app-container">
    <Header />
    <main class="main-content">
      <router-view></router-view>
    </main>
    <Footer />
  </div>
</template>

<script setup>
import Header from './components/common/Header.vue'
import Footer from './components/common/Footer.vue'
</script>

<style scoped>
.app-container {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
.main-content {
  flex: 1;
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px 0;
}
</style>
"""

MALL_FILES["mall-app/src/assets/css/global.css"] = """* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Microsoft YaHei", sans-serif;
}
a {
  text-decoration: none;
  color: #333;
}
ul, li {
  list-style: none;
}
img {
  display: block;
  width: 100%;
  object-fit: cover;
}
button {
  border: none;
  outline: none;
  cursor: pointer;
  background: #e64340;
  color: #fff;
  border-radius: 4px;
}
"""

MALL_FILES["mall-app/src/assets/css/responsive.css"] = """/* 手机端（最大宽度767px） */
@media (max-width: 767px) {
  .goods-list {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 10px !important;
  }
  .detail-container {
    flex-direction: column !important;
  }
  .detail-content {
    flex-direction: column !important;
  }
  .detail-img, .detail-info {
    width: 100% !important;
  }
}

/* 平板端（768px-991px） */
@media (min-width: 768px) and (max-width: 991px) {
  .goods-list {
    grid-template-columns: repeat(3, 1fr) !important;
  }
}

/* PC端（最小宽度992px） */
@media (min-width: 992px) {
  .goods-list {
    grid-template-columns: repeat(4, 1fr) !important;
  }
}
"""

MALL_FILES["mall-app/src/request/index.js"] = """import axios from 'axios'

const http = axios.create({
  baseURL: 'https://portal-api.macrozheng.com/',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json;charset=utf-8'
  }
})

// 请求拦截器：添加token身份认证
http.interceptors.request.use(
  (config) => {
    const token = sessionStorage.getItem('mall_token')
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    console.error('请求错误：', error)
    return Promise.reject(error)
  }
)

// 响应拦截器：统一处理数据、拦截错误
http.interceptors.response.use(
  (response) => {
    return response.data
  },
  (error) => {
    if (error.response.status === 401) {
      sessionStorage.removeItem('mall_token')
      window.location.href = '/#/login'
    } else if (error.response.status === 404) {
      console.error('接口地址不存在')
    } else if (error.response.status === 500) {
      console.error('服务器内部错误')
    }
    return Promise.reject(error)
  }
)

export default http
"""

MALL_FILES["mall-app/src/request/api/goodsApi.js"] = """import http from '../index'

export const goodsApi = {
  // 获取商品列表（GET请求，分页参数）
  getGoodsList: (params) => {
    return http.request({ url: '/home/recommendProductList', method: 'get', params })
  },
  // 获取商品详情（GET请求，动态路由传商品id）
  getGoodsDetail: (id) => {
    return http.request({ url: `/product/detail/${id}`, method: 'get' })
  }
}
"""

MALL_FILES["mall-app/src/store/index.js"] = """import { createStore } from 'vuex'
import goods from './modules/goods'

const store = createStore({
  modules: {
    goods
  }
})

export default store
"""

MALL_FILES["mall-app/src/store/modules/goods/index.js"] = """import state from './states'
import mutations from './mutations'
import getters from './getters'
import actions from './actions'

export default {
  namespaced: true,
  state,
  mutations,
  getters,
  actions
}
"""

MALL_FILES["mall-app/src/store/modules/goods/states.js"] = """export default {
  goodsList: [],
  goodsDetail: {},
  loading: false
}
"""

MALL_FILES["mall-app/src/store/modules/goods/mutations.js"] = """export default {
  SET_GOODS_LIST: (state, list) => {
    state.goodsList = list
  },
  SET_GOODS_DETAIL: (state, detail) => {
    state.goodsDetail = detail
  },
  SET_LOADING: (state, status) => {
    state.loading = status
  }
}
"""

MALL_FILES["mall-app/src/store/modules/goods/getters.js"] = """export default {
  goodsTotal: (state) => state.goodsList.length,
  hotGoods: (state) => state.goodsList.filter(item => item.sale > 500)
}
"""

MALL_FILES["mall-app/src/store/modules/goods/actions.js"] = """import { goodsApi } from '@/request/api/goodsApi'

export default {
  async getGoodsList({ commit }, params) {
    commit('SET_LOADING', true)
    try {
      const res = await goodsApi.getGoodsList(params)
      if (res.code === 200) {
        commit('SET_GOODS_LIST', res.data.product)
      }
    } catch (error) {
      console.error('获取商品列表失败：', error)
    } finally {
      commit('SET_LOADING', false)
    }
  },
  async getGoodsDetail({ commit }, id) {
    commit('SET_LOADING', true)
    try {
      const res = await goodsApi.getGoodsDetail(id)
      if (res.code === 200) {
        commit('SET_GOODS_DETAIL', res.data)
      }
    } catch (error) {
      console.error('获取商品详情失败：', error)
    } finally {
      commit('SET_LOADING', false)
    }
  }
}
"""

MALL_FILES["mall-app/src/router/index.js"] = """import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    redirect: '/home'
  },
  {
    path: '/home',
    name: 'Home',
    component: () => import('@/views/Home.vue'),
    meta: { title: 'Vue3商城 - 首页' }
  },
  {
    path: '/detail/:id',
    name: 'Detail',
    component: () => import('@/views/Detail.vue'),
    meta: { title: 'Vue3商城 - 商品详情' }
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('@/views/NotFound.vue'),
    meta: { title: '页面不存在' }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() {
    return { top: 0 }
  }
})

router.afterEach((to) => {
  if (to.meta.title) {
    document.title = to.meta.title
  }
})

export default router
"""

MALL_FILES["mall-app/src/components/common/Header.vue"] = """<template>
  <header class="header">
    <div class="header-container">
      <h1 class="logo">
        <router-link to="/home">Vue3商城</router-link>
      </h1>
      <nav class="nav">
        <ul>
          <li><router-link to="/home" class="nav-link">首页</router-link></li>
          <li><a href="#" class="nav-link">热销商品</a></li>
          <li><a href="#" class="nav-link">关于我们</a></li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<script setup>
</script>

<style scoped>
.header {
  width: 100%;
  background: #fff;
  border-bottom: 1px solid #eee;
  padding: 10px 0;
  position: sticky;
  top: 0;
  z-index: 999;
}
.header-container {
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.logo a {
  font-size: 24px;
  font-weight: bold;
  color: #e64340;
}
.nav ul {
  display: flex;
  gap: 30px;
}
.nav-link {
  font-size: 16px;
  color: #333;
  transition: color 0.3s;
}
.nav-link:hover,
.nav-link.router-link-active {
  color: #e64340;
}
/* 手机端：导航栏居中 */
@media (max-width: 767px) {
  .header-container {
    flex-direction: column;
    gap: 10px;
  }
}
</style>
"""

MALL_FILES["mall-app/src/components/common/Footer.vue"] = """<template>
  <footer class="footer">
    <div class="footer-container">
      <p>&copy; 2025 Vue3商城 版权所有 | 基于Vue3+Vue Router+Vuex+Axios开发</p>
    </div>
  </footer>
</template>

<script setup>
</script>

<style scoped>
.footer {
  width: 100%;
  background: #333;
  color: #fff;
  text-align: center;
  padding: 20px 0;
  margin-top: 30px;
}
.footer-container {
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
}
</style>
"""

MALL_FILES["mall-app/src/components/common/GoodsItem.vue"] = """<template>
  <div class="goods-item" @click="toDetail(goods.id)">
    <div class="goods-img">
      <img :src="goods.pic" alt="商品图片">
    </div>
    <div class="goods-info">
      <h3 class="goods-name">{{ goods.name }}</h3>
      <div class="goods-price">&yen;{{ goods.price }}</div>
      <div class="goods-sales">销量：{{ goods.sale }}+</div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const props = defineProps({
  goods: {
    type: Object,
    required: true,
    default: () => ({})
  }
})

const router = useRouter()

const toDetail = (id) => {
  router.push(`/detail/${id}`)
}
</script>

<style scoped>
.goods-item {
  border: 1px solid #eee;
  border-radius: 8px;
  overflow: hidden;
  cursor: pointer;
  transition: box-shadow 0.3s;
}
.goods-item:hover {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
.goods-img {
  width: 100%;
}
.goods-info {
  padding: 10px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.goods-name {
  font-size: 16px;
  font-weight: 500;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.goods-price {
  font-size: 18px;
  color: #e64340;
  font-weight: bold;
}
.goods-sales {
  font-size: 14px;
  color: #999;
}
</style>
"""

MALL_FILES["mall-app/src/views/Home.vue"] = """<template>
  <div class="home-container">
    <div class="home-title">
      <h2>商城首页</h2>
      <p>商品总数：{{ goodsTotal }} | 热销商品：{{ hotGoods.length }}</p>
    </div>
    <div class="loading" v-if="loading">加载中...</div>
    <div class="goods-list" v-else>
      <GoodsItem
        v-for="goods in goodsList"
        :key="goods.id"
        :goods="goods"
      />
    </div>
    <div class="no-goods" v-if="!loading && goodsList.length === 0">
      暂无商品数据~
    </div>
  </div>
</template>

<script setup>
import { onMounted, computed } from 'vue'
import { useStore } from 'vuex'
import GoodsItem from '@/components/common/GoodsItem.vue'

const store = useStore()

const goodsList = computed(() => store.state.goods.goodsList)
const loading = computed(() => store.state.goods.loading)
const goodsTotal = computed(() => store.getters['goods/goodsTotal'])
const hotGoods = computed(() => store.getters['goods/hotGoods'])

onMounted(() => {
  store.dispatch('goods/getGoodsList', { pageNum: 1, pageSize: 10 })
})
</script>

<style scoped>
.home-title {
  margin-bottom: 20px;
  padding-bottom: 10px;
  border-bottom: 1px solid #eee;
}
.home-title h2 {
  font-size: 24px;
  color: #333;
  margin-bottom: 8px;
}
.home-title p {
  font-size: 14px;
  color: #999;
}
.loading {
  text-align: center;
  font-size: 18px;
  padding: 50px 0;
  color: #666;
}
.goods-list {
  display: grid;
  gap: 20px;
  width: 100%;
}
.no-goods {
  text-align: center;
  font-size: 16px;
  padding: 50px 0;
  color: #999;
}
</style>
"""

MALL_FILES["mall-app/src/views/Detail.vue"] = """<template>
  <div class="detail-container">
    <div class="loading" v-if="loading">加载中...</div>
    <div class="detail-content" v-else-if="Object.keys(goodsDetail).length > 0">
      <div class="detail-img">
        <img :src="goodsDetail.pic" alt="商品详情图">
      </div>
      <div class="detail-info">
        <h2 class="detail-name">{{ goodsDetail.name }}</h2>
        <div class="detail-price">
          <span class="now-price">&yen;{{ goodsDetail.price }}</span>
          <span class="ori-price">原价：&yen;{{ goodsDetail.originalPrice }}</span>
        </div>
        <div class="detail-count">
          <span>销量：{{ goodsDetail.sale }}+</span>
          <span>库存：{{ goodsDetail.stock }}件</span>
        </div>
        <div class="detail-desc">
          <h3>商品描述：</h3>
          <p>{{ goodsDetail.subTitle }}</p>
        </div>
        <div class="detail-btn">
          <button class="buy-btn">立即购买</button>
          <button class="cart-btn">加入购物车</button>
        </div>
      </div>
    </div>
    <div class="no-detail" v-else>
      暂无商品详情数据~
    </div>
  </div>
</template>

<script setup>
import { onMounted, computed } from 'vue'
import { useStore } from 'vuex'
import { useRoute } from 'vue-router'

const store = useStore()
const route = useRoute()

const goodsDetail = computed(() => store.state.goods.goodsDetail)
const loading = computed(() => store.state.goods.loading)

onMounted(() => {
  const goodsId = route.params.id
  store.dispatch('goods/getGoodsDetail', goodsId)
})
</script>

<style scoped>
.detail-container {
  width: 100%;
  display: flex;
  gap: 30px;
  align-items: flex-start;
}
.detail-content {
  width: 100%;
  display: flex;
}
.loading {
  width: 100%;
  text-align: center;
  font-size: 18px;
  padding: 50px 0;
  color: #666;
}
.detail-img {
  width: 40%;
  border: 1px solid #eee;
  border-radius: 8px;
  overflow: hidden;
}
.detail-info {
  width: 60%;
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.detail-name {
  font-size: 28px;
  color: #333;
  font-weight: bold;
}
.detail-price {
  display: flex;
  gap: 20px;
  align-items: center;
}
.now-price {
  font-size: 32px;
  color: #e64340;
  font-weight: bold;
}
.ori-price {
  font-size: 16px;
  color: #999;
  text-decoration: line-through;
}
.detail-count {
  display: flex;
  gap: 30px;
  font-size: 16px;
  color: #666;
  padding-bottom: 10px;
  border-bottom: 1px dashed #eee;
}
.detail-desc h3 {
  font-size: 20px;
  margin-bottom: 10px;
}
.detail-desc p {
  font-size: 16px;
  line-height: 1.8;
  color: #666;
}
.detail-btn {
  display: flex;
  gap: 20px;
  margin-top: 20px;
}
.detail-btn button {
  padding: 12px 30px;
  font-size: 18px;
}
.cart-btn {
  background: #ff9900;
}
.no-detail {
  width: 100%;
  text-align: center;
  font-size: 16px;
  padding: 50px 0;
  color: #999;
}
</style>
"""

MALL_FILES["mall-app/src/views/NotFound.vue"] = """<template>
  <div class="not-found">
    <h2>404 - 页面不存在</h2>
    <router-link to="/home" class="back-home">返回商城首页</router-link>
  </div>
</template>

<script setup>
</script>

<style scoped>
.not-found {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 20px;
}
.back-home {
  padding: 10px 20px;
  background: #e64340;
  color: #fff;
  border-radius: 4px;
}
</style>
"""

# ═══════════════════════════════════════════════════════════════════════
# Write all files
# ═══════════════════════════════════════════════════════════════════════

def create_project(project_name, files):
    """Create project directory and write all files."""
    for relpath, content in files.items():
        full_path = f"{BASE}/{relpath}"
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content.lstrip('\n'))
        print(f"  Created: {relpath}")


if __name__ == "__main__":
    print("=== Creating vue3-todo-app (实验七) ===")
    create_project("vue3-todo-app", TODO_FILES)

    print("\n=== Creating mall-app (实验八) ===")
    create_project("mall-app", MALL_FILES)

    print(f"\nAll files created under: {BASE}")
    print("\nNext steps:")
    print("  1. Open each project folder in HBuilderX")
    print("  2. Run 'npm install' in terminal")
    print("  3. Run 'npm run dev' to start")
