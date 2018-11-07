using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace File_Splitter
{
    public partial class frmMain : Form
    {
        public frmMain()
        {
            InitializeComponent();
        }

        private void btnBrowseFile_Click(object sender, EventArgs e)
        {
            DialogResult result = openFileDialog1.ShowDialog();
            openFileDialog1.Title = "File to split";
            openFileDialog1.InitialDirectory = Path.GetDirectoryName(Application.ExecutablePath);
            if (result == DialogResult.OK)
            {
                txtFile.Text = openFileDialog1.FileName;
                try
                {
                    
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Err: " + ex.Message);
                }
            }
        }

        private void btnBrowseDirectory_Click(object sender, EventArgs e)
        {

        }
    }
}
