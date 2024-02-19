import React, { useState } from 'react'

export const TwoPaneList = ({ data }) => {
  const [selectedTitle, setSelectedTitle] = useState(null);

  // Function to handle title click
  const handleTitleClick = title => {
    setSelectedTitle(title);
  };

  // Find the selected item's content
  const selectedItem = data.find(item => item.title === selectedTitle);

  return (
    <div className="columns">
      <div className="column is-one-third">
        <aside className="menu">
          <ul className="menu-list">
            {data.map(item => (
              <li key={item.title}>
                <a onClick={() => handleTitleClick(item.title)}>{item.title}</a>
              </li>
            ))}
          </ul>
        </aside>
      </div>
      <div className="column">
        {selectedItem ? (
          selectedItem.content.map((paragraph, index) => (
            <p key={index}>{paragraph}</p>
          ))
        ) : (
          <div>Please select a title from the list to display its content.</div>
        )}
      </div>
    </div>
  );
};
