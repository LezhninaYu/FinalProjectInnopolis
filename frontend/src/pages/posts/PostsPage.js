import React, { useState, useEffect } from 'react';
import Header from '../../components/Header/Header';
import PostCard from '../../components/PostCard/PostCard';
import styles from './PostsPage.module.css';
import API from '../../api';

export default function PostsPage() {
  const [posts, setPosts] = useState([]);

  async function getPosts() {
    const postsResponse = await API.get(`/post`);
    setPosts(postsResponse.data.posts);
  }

  useEffect(() => {
    getPosts();
  }, []);

  const handleDelete = async id => {
    setPosts(posts.filter(item => item.id !== id));
    const deleteResponse = await API.delete(`/post/${id}`);
    console.log(deleteResponse.data);
  };

  return (
    <>
      <Header props={false} />
      <section className={styles.section}>
        {!posts.length ? (
          <h2 className={styles.card}>Пока нет постов!</h2>
        ) : (
          posts.map(post => {
            return (
              <PostCard key={post.id} post={post} handleDelete={handleDelete} />
            );
          })
        )}
      </section>
    </>
  );
}
