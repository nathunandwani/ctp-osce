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
            }
        }

        private void btnBrowseDirectory_Click(object sender, EventArgs e)
        {
            DialogResult result = folderBrowserDialog1.ShowDialog();
            if (result == DialogResult.OK)
            {
                txtDirectoryOutput.Text = folderBrowserDialog1.SelectedPath + "\\";
            }
        }

        private void btnSplit_Click(object sender, EventArgs e)
        {
            int bytes = 0;
            try
            {
                bytes = Convert.ToInt32(txtNumBytes.Text);
            }
            catch (Exception ex) 
            {
                MessageBox.Show("Err: " + ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            if (bytes <= 0) 
            {
                MessageBox.Show("Err: Byte increment cannot be zero or negative in value!", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            if (File.Exists(txtFile.Text))
            {
                if (!Directory.Exists(txtDirectoryOutput.Text))
                {
                    Directory.CreateDirectory(txtDirectoryOutput.Text);
                }
                byte[] file = File.ReadAllBytes(txtFile.Text);
                int counter = bytes;
                string filename = Path.GetFileNameWithoutExtension(txtFile.Text);
                for (int i = counter; i < file.Length; i++) 
                {
                    List<byte> splitted = new List<byte>();
                    for (int j = 0; j < i; j++) 
                    {
                        splitted.Add(file[j]);
                    }
                    File.WriteAllBytes(txtDirectoryOutput.Text + filename + i.ToString(), splitted.ToArray());
                    counter += bytes;
                }
                MessageBox.Show("Done!", "Success", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            else 
            {
                MessageBox.Show("Err: File doesn't exist!", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
}
