import React, { useState } from 'react';

export const ItemList = () => {
  const [items, setItems] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [editIndex, setEditIndex] = useState(null);
  const [editValue, setEditValue] = useState('');

  // Handles adding a new item to the list
  const handleAdd = (e) => {
    e.preventDefault();
    if (!inputValue.trim()) return;
    setItems([...items, inputValue]);
    setInputValue('');
  };
  // Handles deleting an item from the list
  const handleDelete = (index) => {
    if (window.confirm('Are you sure you want to delete this item?')) {
      setItems(items.filter((_, i) => i !== index));
    }
  };
  // Prepares an item for editing by setting its index and current value
  const handleEdit = (index) => {
    setEditIndex(index);
    setEditValue(items[index]);
  };
  // Updates the edit value as the user types in the edit field
  const handleEditChange = (e) => {
    setEditValue(e.target.value);
  };
  // Submits the edited item's new value, updating the list
  const handleEditSubmit = (e, index) => {
    e.preventDefault();
    const newItems = [...items];
    newItems[index] = editValue;
    setItems(newItems);
    setEditIndex(null);
  };

  return (
    <div>
      {items.map((item, index) => (
        index === editIndex ? (
          <form onSubmit={(e) => handleEditSubmit(e, index)} key={index}>
            <input className="input" type="text" value={editValue} onChange={handleEditChange} autoFocus />
          </form>
        ) : (
          <div className="is-flex is-align-items-center" key={index}>
            <button className="button is-small is-danger" onClick={() => handleDelete(index)}>Delete</button>
            <button className="button is-small is-info" onClick={() => handleEdit(index)}>Edit</button>
            <p className="mx-2">{item}</p>
          </div>
        )
      ))}
      <form onSubmit={handleAdd}>
        <input className="input" type="text" value={inputValue} onChange={(e) => setInputValue(e.target.value)} placeholder="Add new item" />
      </form>
    </div>
  );
};
