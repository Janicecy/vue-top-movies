import VueRouter from 'vue-router'
import Home from '../pages/Home'
import MovieList from '../pages/MovieList'
import Rating from '../pages/Rating'
export default new VueRouter({
    mode:'history',
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
            name: 'rating',
            path: '/rating',
            component: Rating
        }
        
    ]
})