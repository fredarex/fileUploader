import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"
import { Button, LinearProgress, Slider} from "@mui/material"
import { styled,makeStyles } from "@mui/styles"

interface State {
  numClicks: number
  isFocused: boolean
}

const useStyles = makeStyles((theme) => ({
  root: {
    '& > *': {
      margin: theme.spacing(1),
    },
  },
  input: {
    display: 'none',
  },
}));

/**
 * This is a React-based component template. The `render()` function is called
 * automatically when your component should be re-rendered.
 * 
 * 
 */




class MyFileupload extends StreamlitComponentBase<State> {
  public state = { uploaded: true,uploadedProgress:30}

  public render = (): ReactNode => {
    const classes = useStyles();
    return (
      <div>
        <LinearProgress variant="determinate" value={this.state.uploadedProgress} />
        <input
          accept="image/*"
          className={classes.input}
          id="contained-button-file"
          multiple
          type="file"
          onClick={this.onClicked}
        />
        
        <label htmlFor="contained-button-file">
          <Button variant="contained" color="primary" component="span">
            Upload
          </Button>
        </label>
      </div>
    )
  }

  /** Click handler for our "Click Me!" button. */
  private onClicked = (): void => {
    // Increment state.numClicks, and pass the new value back to
    // Streamlit via `Streamlit.setComponentValue`.

    // Streamlit.setComponentValue("returning plenty value")

    this.setState(
      prevState => ({ uploaded: !this.state.uploaded }),
      () => Streamlit.setComponentValue(!this.state.uploaded)
    )
  }

}

  /** Focus handler for our "Click Me!" button. */
 

// "withStreamlitConnection" is a wrapper function. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).
export default withStreamlitConnection(MyFileupload)
