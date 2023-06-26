import VueRouter from 'vue-router'
import Home from '../pages/Home'
import MovieList from '../pages/MovieList'
import Rating from '../pages/Rating'
import { publicPath } from '../../vue.config'
export default new VueRouter({
    mode:'history',
    base: publicPath,
    routes: [
        {
            path: '/', redirect: '/home'
        },
        {
            name: 'home',
            path: '/home',
            component: Home
        },
        {
            name: 'movie',
            path: '/movie',
            component: MovieList
        },
        {
            name: 'chart',
            path: '/charts',
            component: Rating
        },
        {
            name: 'Analytics',
            path: '/analytics',
            component: Rating
        }
        
    ]
})