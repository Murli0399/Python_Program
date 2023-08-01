import React, { useState } from "react";
import "./App.css";

function App() {
  const [posts, setPosts] = useState([]);
  const [newPost, setNewPost] = useState({ username: "", caption: "" });

  const inputChange = (e) => {
    setNewPost({ ...newPost, [e.target.name]: e.target.value });
  };

  const postSubmit = (e) => {
    e.preventDefault();
    const updatedPost = [...posts, newPost];
    setPosts(updatedPost);
    setNewPost({ username: "", caption: "" });
  };

  const postDelete = (index) => {
    const updatedPosts = [...posts];
    updatedPosts.splice(index, 1);
    setPosts(updatedPosts);
  };

  return (
    <div>
      <h1>Instagram Like Web App</h1>
      <form onSubmit={postSubmit}>
        <input
          type="text"
          name="username"
          placeholder="UserName"
          value={newPost.username}
          onChange={inputChange}
        />
        <input
          type="text"
          name="caption"
          placeholder="Caption"
          value={newPost.caption}
          onChange={inputChange}
        />
        <button type="submit">Add Post</button>
      </form>
      <h2>Posts</h2>
      {posts.length === 0 ? (
        <p>No posts yet.</p>
      ) : (
        <ul>
          {posts.map((post, index) => (
            <li key={index}>
              <strong>{post.username}</strong> - {post.caption}
              {post.likes && <span> - Likes: {post.likes}</span>}
              {post.comments && (
                <ul>
                  {post.comments.map((comment, commentIndex) => (
                    <li key={commentIndex}>{comment}</li>
                  ))}
                </ul>
              )}
              <button onClick={() => postDelete(index)}>Delete</button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
