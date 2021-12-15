import React, { useContext, useState, useEffect } from 'react';
import { AuthContext } from '../../context';
import styles from './PostCard.module.css';
import API from '../../api';

const PostCard = ({ post, handleDelete }) => {
  const { isAuth } = useContext(AuthContext);
  const [id, setId] = useState(-1);
  const [title, setTitle] = useState('');
  const [body, setBody] = useState('');
  const [isEdited, setIsEdited] = useState(false);

  useEffect(() => {
    setTitle(post.name);
    setBody(post.text);
    setId(post.id)
  }, [post]);

  const handleTitle = (e) => {
    setTitle(e.target.value);
  }

  const handleBody = (e) => {
    setBody(e.target.value);
  }

  const handleEdit = async () => {
    if (isEdited) {

      const postData = {
        name: title,
        text: body,
        user_id: 0
      }

      const editResponse = await API.put(`/post/${id}`, postData);
      console.log(editResponse.data);
      setIsEdited(!isEdited);
    }
    setIsEdited(!isEdited);
  };

  return (
    <div className={styles.card}>
      {isEdited ? (
        <div className={styles.titleInputContainer}>
          <input type="text" className={styles.titleInput} onChange={handleTitle} value={title} />
        </div>
      ) : (
        <h2 className={styles.title}>{title}</h2>
      )}
      {isEdited ? (
        <textarea cols='100' rows='8' value={body} onChange={handleBody} className={styles.textInput} />
      ) : (
        <p className={styles.text}>{body}</p>
      )}
      <div className={styles.btnContainer}>
        {isAuth && (
          <button className={styles.editBtn} onClick={handleEdit}>
            {isEdited ? 'Сохранить' : 'Редактировать'}
          </button>
        )}
        {isAuth && <button onClick={() => handleDelete(id)} className={styles.deleteBtn}>Удалить</button>}
      </div>
    </div>
  );
};

export default PostCard;
