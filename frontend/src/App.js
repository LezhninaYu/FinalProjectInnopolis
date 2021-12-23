import React, { useEffect, useState } from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { AuthContext } from './context';
import AuthPage from './pages/auth/AuthPage';
import AboutPage from './pages/about/AboutPage';
import LandingPage from './pages/landing/LandingPage';
import PostsPage from './pages/posts/PostsPage';
import ErrorPage from './pages/system/ErrorPage';
import ProtectedRoute from './components/ProtectedRoute';

export default function App() {
  const [isAuth, setisAuth] = useState(false);
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    if (localStorage.getItem('isAuth')) {
      setisAuth(true);
    }
  }, []);

  return (
    <AuthContext.Provider value={{ isAuth, setisAuth, posts, setPosts }}>
      <BrowserRouter>
        <Routes>
          <Route
            exact
            path='/posts'
            element={
              <ProtectedRoute>
                <PostsPage />
              </ProtectedRoute>
            }
          />
          <Route exact path='/' element={<LandingPage />} />
          <Route exact path='/login' element={<AuthPage />} />
          <Route exact path='/about' element={<AboutPage />} />
          <Route exact path='/posts' element={<PostsPage />} />
          <Route exact path='*' element={<ErrorPage />} />
        </Routes>
      </BrowserRouter>
    </AuthContext.Provider>
  );
}
